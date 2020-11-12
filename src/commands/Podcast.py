from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parseTracks


class Podcast(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PODCAST_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        trackOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
        results = self.spotify.search(
            q=query, limit=int(getSetting("MAX_RESULTS")), offset=trackOffset, type="show")
        return self.ParsePodcasts(results)

    def Run(self, data: str):
        raise NotImplementedError

    def ParsePodcasts(self, results):
        parsedResults = []
        for show in results["shows"]["items"]:
            parsedResults.append(
                (show["uri"], show["name"] + " - " + show["publisher"], "Spotify", 100, 100, {}))
        if(not parsedResults):
            parsedResults.append(
                ("", "No podcasts found!", "Spotify", 100, 100, {}))
        return parsedResults
