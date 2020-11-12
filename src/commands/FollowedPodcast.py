from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery
import dbus.service

iface = "org.kde.krunner1"

class FollowedPodcast(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("FOLLOWED_PODCAST_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        savedShowsOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
        savedShows = self.spotify.current_user_saved_shows(offset=savedShowsOffset, limit=int(getSetting("MAX_RESULTS")))
        shows = []
        for show in savedShows['items']:
            name = show['show']['name']
            uri = show['show']['uri']
            shows.append((uri, name, "Spotify", 100, 100, {"actions": ["asdf"]}))
        if(len(shows) > 0):
            return shows
        return [("", "No podcast is being followed!", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        raise NotImplementedError
        
