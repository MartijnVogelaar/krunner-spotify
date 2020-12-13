from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parseArtists


class Artist(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_ARTIST_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        searchResults = []
        if(query != ""):
            query = "artist:" + query
            trackOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
            searchResults = self.spotify.search(query, int(
                getSetting("MAX_RESULTS")), trackOffset, "artist")['artists']
        else:
            searchResults = self.spotify.current_user_top_artists(
                limit=int(getSetting("MAX_RESULTS")))
        return parseArtists(searchResults)

    def Run(self, data: str):
        raise NotImplementedError
