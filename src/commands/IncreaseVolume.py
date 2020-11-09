from .Command import Command
from Config import getCommandName

DEVICES_WITHOUT_VOLUME_CONTROL = ["Tablet", "Smartphone"]


class IncreaseVolume(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("INCREASE_VOLUME_COMMAND"), spotify)
        self.currentVolume = self.spotify.current_playback()[
            "device"]["volume_percent"]

    def Match(self, query: str):
        if(self.spotify.current_playback()["device"]["type"] in DEVICES_WITHOUT_VOLUME_CONTROL):
            return [("", "Volume cannot be controlled on the current device", "Spotify", 100, 100, {})]
        if(self.currentVolume == 100):
            return [("", "Volume is already 100%", "Spotify", 100, 100, {})]

        query = query.strip(" ")
        if(query.isnumeric()):
            volume = int(query)
            if(volume < 0 or volume > 100):
                return [(" ", "Volume has to be between 1 and 100%", "Spotify", 100, 100, {})]
            else:
                return [(self.command + " " + str(volume), "Increase volume with " + str(volume) + "%", "Spotify", 100, 100, {})]

        return [
            (self.command + " 10", "Increase volume with 10%", "Spotify", 100, 100, {}),
            (self.command + " 25", "Increase volume with 25%", "Spotify", 100, 80, {}),
            (self.command + " 50", "Increase volume with 50%", "Spotify", 100, 60, {}),
            (self.command + " 100", "Increase volume with 100%", "Spotify", 100, 40, {})]

    def Run(self, data: str):
        newVolume = self.currentVolume + int(data)
        newVolume = newVolume if newVolume < 100 else 100
        self.spotify.volume(newVolume)
