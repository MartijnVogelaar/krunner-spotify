from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parseTracks

class Song(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_SONG_COMMAND"), spotify)

    def Match(self, query: str):
        searchResults = []
        if(query != ""):
            query, page = parseSearchQuery(query)
            trackOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
            searchResults = self.spotify.search(
                query, int(getSetting("MAX_RESULTS")), trackOffset, "track")
        else:
            searchResults = {"tracks": self.spotify.current_user_top_tracks(offset = 0, limit = int(getSetting("MAX_RESULTS")))}
        return parseTracks(searchResults)

    def Run(self, data: str):
        raise NotImplementedError
