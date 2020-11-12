from .Command import Command
from .ArtistSong import ArtistSong
from .FeaturedPlaylist import FeaturedPlaylist
from .Playlist import Playlist
from .Song import Song
from .MyPlaylist import MyPlaylist
from .FollowedPodcast import FollowedPodcast
from .Podcast import Podcast
from Config import getCommandName, getSetting


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
        if("track" in data or "episode" in data):
            self.spotify.start_playback(uris=[data])
        else:
            self.spotify.start_playback(context_uri=data)

    def executeCommand(self, command: str):
        if(getSetting("CASE_SENSITIVE") == "False"):
            command = command.upper()
        if(command == getCommandName('PLAY_SONG_COMMAND')):
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
        raise RuntimeError("Incorrect command")
