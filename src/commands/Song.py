from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parseTracks


class Song(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_SONG_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        trackOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
        results = self.spotify.search(
            query, int(getSetting("MAX_RESULTS")), trackOffset, "track")
        return parseTracks(results)

    def Run(self, data: str):
        raise NotImplementedError
