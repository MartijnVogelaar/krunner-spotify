from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parseTracks

class ArtistSong(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_SONG_BY_ARTIST_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        searchResults = []
        if(query != ""):
            query = "artist:" + query
            trackOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
            searchResults = self.spotify.search(query, int(
                getSetting("MAX_RESULTS")), trackOffset, "track")
        else:
            topArtist = self.spotify.current_user_top_artists(limit = 1)
            result = self.spotify.artist_top_tracks(topArtist['items'][0]['id'])
            searchResults = {"tracks": {"items" : result["tracks"]}}

        return parseTracks(searchResults)

    def Run(self, data: str):
        raise NotImplementedError
