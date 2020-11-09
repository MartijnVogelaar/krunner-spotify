from .Command import Command
from Config import getCommandName


class Next(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("NEXT_COMMAND"), spotify)

    def Match(self, query: str):
        return [(self.command, "Skip current track", "Spotify", 100, 100, {}), ]

    def Run(self, data: str):
        self.spotify.next_track()
