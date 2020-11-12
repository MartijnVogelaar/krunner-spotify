from .Command import Command
from Config import getCommandName
from Util import parseSearchQuery
from Config import getSetting, getCommandName


class Episode(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("EPISODE_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        episodeOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
        playbackDetails = self.spotify.currently_playing(
            additional_types="episode")
        if(playbackDetails["item"]["type"] == "episode"):
            episodes = self.spotify.show_episodes(
                playbackDetails["item"]["show"]['id'], offset=episodeOffset, limit=int(getSetting("MAX_RESULTS")))
            episodeResults = []
            relevance = 100
            for episode in episodes['items']:
                icon = self.GetIcon(episode, playbackDetails)
                episodeResults.append((episode["uri"],
                                       episode["name"],
                                       icon,
                                       relevance, 100, {}))
                relevance = relevance - 1
            return episodeResults
        else:
            return [("", "No podcast is being played!", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        raise NotImplementedError

    def GetIcon(self, episode, playbackDetails):
        icon = "NewSpotify"
        if episode["resume_point"]["resume_position_ms"] != 0:
            icon = "ResumeSpotify"
        if episode["resume_point"]["fully_played"]:
            icon = "FullyPlayedSpotify"
        if episode["id"] == playbackDetails["item"]["id"]:
            icon = "CurrentlyPlayingSpotify"
        return icon
