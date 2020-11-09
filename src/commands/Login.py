from .Command import Command
from Config import getCommandName, getSetting
import os


class Login(Command):
    def __init__(self, spotify):
        try:
            super().__init__(getCommandName("LOGIN_COMMAND"), spotify)
        except RuntimeError:
            pass

    def Match(self, query: str):
        if(not os.path.isfile(getSetting("CACHE_PATH"))):
            return [(getCommandName("LOGIN_COMMAND"), "Log into Spotify", "Spotify", 100, 100, {})]
        else:
            return [("", "Already logged in", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        self.spotify.current_user()
