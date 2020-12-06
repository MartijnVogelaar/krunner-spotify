from .Command import Command
from Config import getCommandName, getSetting

DEVICES_WITHOUT_VOLUME_CONTROL = ["Tablet", "Smartphone"]


class IncreaseVolume(Command):
    plusCount = 0
    currentVolume = 0

    def __init__(self, spotify):
        super().__init__(getCommandName("INCREASE_VOLUME_COMMAND"), spotify)

    def Match(self, query: str):
        if(IncreaseVolume.plusCount == 0):
            IncreaseVolume.currentVolume = self.spotify.current_playback()[
                "device"]["volume_percent"]
        if(self.spotify.current_playback()["device"]["type"] in DEVICES_WITHOUT_VOLUME_CONTROL):
            return [("", "Volume cannot be controlled on the current device", "Spotify", 100, 100, {})]

        query = query.strip(" ")
        returnOptions = []
        if(query.isnumeric() and len(query) > 0):
            returnOptions = self.increaseByValue(query)
        elif(len(query) > 0 and query[0] == "+" and query == len(query) * query[0]):
            returnOptions = self.IncreaseByPlusCharacter(query)
            
        self.spotify.volume(IncreaseVolume.currentVolume)
        return returnOptions if returnOptions != [] else self.IncreaseByChoice()

    def Run(self, data: str):
        IncreaseVolume.currentVolume = IncreaseVolume.currentVolume + int(data)
        IncreaseVolume.currentVolume = IncreaseVolume.currentVolume if IncreaseVolume.currentVolume < 100 else 100
        self.spotify.volume(IncreaseVolume.currentVolume)

    def increaseByValue(self, query):
        volume = int(query)
        if(volume < 0 or volume > 100):
            return [(" ", "Volume has to be between 1 and 100%", "Spotify", 100, 100, {})]
        elif(IncreaseVolume.currentVolume == 100):
            return [("", "Volume is already 100%", "Spotify", 100, 100, {})]
        else:
            return [(self.command + " " + str(volume), "Increase volume with " + str(volume) + "%", "Spotify", 100, 100, {})]

    def IncreaseByPlusCharacter(self, query):
        plusDifference = len(query) - IncreaseVolume.plusCount
        IncreaseVolume.plusCount = len(query)
        if(0 == abs(plusDifference) or abs(plusDifference) == 1):
            if(plusDifference == 0):
                plusDifference = 1
            IncreaseVolume.currentVolume = IncreaseVolume.currentVolume + int(getSetting("VOLUME_STEP")) * plusDifference
            if(IncreaseVolume.currentVolume > 100):
                IncreaseVolume.currentVolume = 100
                return [("", "Volume is already 100%", "Spotify", 100, 100, {})]
            if(IncreaseVolume.currentVolume < 0):
                IncreaseVolume.currentVolume = 0
                return [("", "Volume is already 0%", "Spotify", 100, 100, {})]
            else:
                return [("", "Volume is now set to: " + str(IncreaseVolume.currentVolume), "Spotify", 100, 100, {})]
        return []

    def IncreaseByChoice(self):
        if(IncreaseVolume.currentVolume >= 100):
            return [("", "Volume is already 100%", "Spotify", 100, 100, {})]
        else:
            return [
                (self.command + " 10", "Increase volume with 10%",
                 "Spotify", 100, 100, {}),
                (self.command + " 25", "Increase volume with 25%",
                 "Spotify", 100, 80, {}),
                (self.command + " 50", "Increase volume with 50%",
                 "Spotify", 100, 60, {}),
                (self.command + " 100", "Increase volume with 100%", "Spotify", 100, 40, {})]
