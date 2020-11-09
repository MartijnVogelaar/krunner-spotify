from .Command import Command
from Config import getCommandName, getSetting
import webbrowser


class StartSpotify(Command):
    def __init__(self, spotify):
        try:
            super().__init__(getCommandName("START_SPOTIFY_COMMAND"), spotify)
            self.spotifyStarted = True
        except RuntimeError:
            self.spotifyStarted = False

    def Match(self, query: str):
        resultText = "Start spotify in browser!"
        if(self.spotifyStarted):
            resultText = "Playback device is available, start new!"
        return [(self.command, resultText, "Spotify", 100, 100, {})]

    def Run(self, data: str):
        webbrowser.open(getSetting("SPOTIFY_URL"))
