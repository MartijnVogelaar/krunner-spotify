from .Command import Command
from Config import getCommandName, getSetting
import os


class Logout(Command):
    def __init__(self, spotify):
        try:
            super().__init__(getCommandName("LOGOUT_COMMAND"), spotify)
        except RuntimeError:
            pass

    def Match(self, query: str):
        if(os.path.isfile(getSetting("CACHE_PATH"))):
            return [(self.command, "Log out from spotify", "Spotify", 100, 100, {})]
        else:
            return [("", "Not logged in", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        if(os.path.isfile(getSetting("CACHE_PATH"))):
            os.remove(getSetting("CACHE_PATH"))
