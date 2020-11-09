from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parsePlaylists


class FeaturedPlaylist(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_FEATURED_PLAYLIST_COMMAND"), spotify)

    def Match(self, query: str):
        query, page = parseSearchQuery(query)
        playlistOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
        searchResults = self.spotify.featured_playlists(
            limit=int(getSetting("MAX_RESULTS")), offset=playlistOffset)
        return parsePlaylists(searchResults["playlists"])

    def Run(self, data: str):
        raise NotImplementedError
