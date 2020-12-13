from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parseArtists


class TopArtist(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_TOP_ARTIST_COMMAND"), spotify)

    def Match(self, query: str):
        query = "a " + query
        query, page = parseSearchQuery(query)
        trackOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
        searchResults = self.spotify.current_user_top_artists(
                limit=int(getSetting("MAX_RESULTS")), offset = trackOffset)
        return parseArtists(searchResults)

    def Run(self, data: str):
        raise NotImplementedError
