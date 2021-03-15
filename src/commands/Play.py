from .Command import Command
from .ArtistSong import ArtistSong
from .Artist import Artist
from .FeaturedPlaylist import FeaturedPlaylist
from .Playlist import Playlist
from .Song import Song
from .MyPlaylist import MyPlaylist
from .FollowedPodcast import FollowedPodcast
from .Podcast import Podcast
from .Episode import Episode
from .TopArtist import TopArtist
from Config import getCommandName, getSetting

import webbrowser
import re
import time

class Play(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName('PLAY_COMMAND'), spotify)

    def Match(self, query: str):
        arguments = ""
        if(" " in query):
            command, arguments = query.split(" ", 1)
        else:
            command = query

        try:
            results = self.executeCommand(command).Match(arguments)
            for i in range(0, len(results)):
                tempResult = list(results[i])
                tempResult[0] = self.command + " " + tempResult[0]
                results[i] = tuple(tempResult)
            return results
        except RuntimeError:
            return [("", "Invalid command", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        if(not self.spotify.current_playback()):
            # Spotify  only supports uris to be autoplayed if it is a track. Other source such as:
            # Podcasts, Albums, Artists and Playlists cannot be outplayed at this point in time.
            # As we want these source to be autoplayed the following workaround has been made:
            # We first start a "bank" track without sound, we then wait untill the device is playing".
            # When the device is playing we play the actual "wanted" source which now plays automatically.
            
            webbrowser.open("https://open.spotify.com/track/1KMgqD5AFo1hCjEpv50LwR?si=768a514adc444958")
            hasToEndBy = time.time() + 5
            while(not self.spotify.current_playback() ):
                time.sleep(0.1)
                if(time.time() > hasToEndBy):
                    raise RuntimeError("Playback device not started in the specified time.")
                    print("test")
                    return
            self.Run(data)
        elif("track" in data or "episode" in data):
            self.spotify.start_playback(uris=[data])
        elif("show" in data or "artist" in data or "playlist" in data):
            self.spotify.start_playback(context_uri=data)

    def executeCommand(self, command: str):
        if(getSetting("CASE_SENSITIVE") == "False"):
            command = command.upper()
        if(command == getCommandName('PLAY_ARTIST_COMMAND')):
            return Artist(self.spotify)
        elif(command == getCommandName('PLAY_SONG_COMMAND')):
            return Song(self.spotify)
        elif(command == getCommandName('PLAY_SONG_BY_ARTIST_COMMAND')):
            return ArtistSong(self.spotify)
        elif(command == getCommandName('PLAY_FEATURED_PLAYLIST_COMMAND')):
            return FeaturedPlaylist(self.spotify)
        elif(command == getCommandName('PLAY_PLAYLIST_COMMAND')):
            return Playlist(self.spotify)
        elif(command == getCommandName('PLAY_MY_PLAYLIST_COMMAND')):
            return MyPlaylist(self.spotify)
        elif(command == getCommandName("FOLLOWED_PODCAST_COMMAND")):
            return FollowedPodcast(self.spotify)
        elif(command == getCommandName("PODCAST_COMMAND")):
            return Podcast(self.spotify)
        elif(command == getCommandName("EPISODE_COMMAND")):
            return Episode(self.spotify)
        elif(command == getCommandName("PLAY_TOP_ARTIST_COMMAND")):
            return TopArtist(self.spotify)
        raise RuntimeError("Incorrect command")
