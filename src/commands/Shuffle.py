from .Command import Command
from Config import getCommandName

class Shuffle(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("SHUFFLE_COMMAND"), spotify)

    def Match(self, query: str):
        currentPlayback = self.spotify.current_playback()
        state = "Enable"
        if(currentPlayback["shuffle_state"]):
            state = "Disable"
        return [(self.command + " " + state, state + " shuffle", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        if(data == "Enable"):
            self.spotify.shuffle(True)
        else:
            self.spotify.shuffle(False)
