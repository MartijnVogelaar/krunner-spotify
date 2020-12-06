from .Command import Command
from Config import getCommandName, getSetting

DEVICES_WITHOUT_VOLUME_CONTROL = ["Tablet", "Smartphone"]


class DecreaseVolume(Command):
    minusCount = 0
    currentVolume = 0

    def __init__(self, spotify):
        super().__init__(getCommandName("DECREASE_VOLUME_COMMAND"), spotify)

    def Match(self, query: str):
        if(DecreaseVolume.minusCount == 0):
            DecreaseVolume.currentVolume = self.spotify.current_playback()[
                "device"]["volume_percent"]
        if(self.spotify.current_playback()["device"]["type"] in DEVICES_WITHOUT_VOLUME_CONTROL):
            return [("", "Volume cannot be controlled on the current device", "Spotify", 100, 100, {})]

        query = query.strip(" ")
        returnOptions = []
        if(query.isnumeric() and len(query) > 0):
            returnOptions = self.DecreaseByValue(query)
        elif(len(query) > 0 and query[0] == "-" and query == len(query) * query[0]):
            returnOptions = self.DecreaseByMinusCharacter(query)
        
        self.spotify.volume(DecreaseVolume.currentVolume)
        return returnOptions if returnOptions != [] else self.DecreaseByChoice()

    def Run(self, data: str):
        DecreaseVolume.currentVolume = DecreaseVolume.currentVolume - int(data)
        DecreaseVolume.currentVolume = DecreaseVolume.currentVolume if DecreaseVolume.currentVolume > 0 else 0
        self.spotify.volume(DecreaseVolume.currentVolume)

    def DecreaseByValue(self, query):
        volume = int(query)
        if(volume < 0 or volume > 100):
            return [("", "Volume has to be between 1 and 100%", "Spotify", 100, 100, {})]
        elif(DecreaseVolume.currentVolume == 0):
            return [("", "Volume is already 0%", "Spotify", 100, 100, {})]
        else:
            return [(self.command + " " + str(volume), "Decrease volume with " + str(volume) + "%", "Spotify", 100, 100, {})]

    def DecreaseByMinusCharacter(self, query):
        minusDifference = len(query) - DecreaseVolume.minusCount
        DecreaseVolume.minusCount = len(query)
        if(0 == abs(minusDifference) or abs(minusDifference) == 1):
            if(minusDifference == 0):
                minusDifference = 1
            DecreaseVolume.currentVolume = DecreaseVolume.currentVolume - int(getSetting("VOLUME_STEP")) * minusDifference
            if(DecreaseVolume.currentVolume > 100):
                DecreaseVolume.currentVolume = 100
                return [("", "Volume is already 100%", "Spotify", 100, 100, {})]
            if(DecreaseVolume.currentVolume < 0):
                DecreaseVolume.currentVolume = 0
                return [("", "Volume is already 0%", "Spotify", 100, 100, {})]
            else:
                return [("", "Volume is now set to: " + str(DecreaseVolume.currentVolume), "Spotify", 100, 100, {})]
        return []

    def DecreaseByChoice(self):
        if(DecreaseVolume.currentVolume <= 0):
            return [("", "Volume is already 0%", "Spotify", 100, 100, {})]
        else:
            return [
                (self.command + " 10", "Decrease volume with 10%",
                 "Spotify", 100, 100, {}),
                (self.command + " 25", "Decrease volume with 25%",
                 "Spotify", 100, 80, {}),
                (self.command + " 50", "Decrease volume with 50%",
                 "Spotify", 100, 60, {}),
                (self.command + " 100", "Decrease volume with 100%", "Spotify", 100, 40, {})]
