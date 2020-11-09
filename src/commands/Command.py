from abc import ABC
from Config import getSetting
import os


class Command(ABC):
    def __init__(self, command, spotify):
        self.spotify = spotify
        self.command = command
        if(not os.path.isfile(getSetting("CACHE_PATH"))):
            raise RuntimeError("Not logged in!")
        if(not self.spotify.current_playback()):
            raise RuntimeError("No playback device available!")

    def Match(self, query: str):
        pass

    def Run(self, data: str):
        pass
