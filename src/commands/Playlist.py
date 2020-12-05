from .Command import Command
from Config import getCommandName, getSetting
from Util import parseSearchQuery, parsePlaylists


class Playlist(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PLAY_PLAYLIST_COMMAND"), spotify)

    def Match(self, query: str):
        searchResults = []
        if(query != ""):
            query, page = parseSearchQuery(query)
            playlistOffset = int(getSetting("MAX_RESULTS")) * (page - 1)
            searchResults = self.spotify.search(
                query, int(getSetting("MAX_RESULTS")), playlistOffset, "playlist")
        else:
            searchResults = self.spotify.featured_playlists(
                limit=int(getSetting("MAX_RESULTS")))
        return parsePlaylists(searchResults["playlists"])

    def Run(self, data: str):
        raise NotImplementedError
