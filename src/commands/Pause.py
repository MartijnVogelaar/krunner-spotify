from .Command import Command
from Config import getCommandName


class Pause(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("PAUSE_COMMAND"), spotify)

    def Match(self, query: str):
        return [(self.command, "Pause current song", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        self.spotify.pause_playback()
