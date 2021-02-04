from .Command import Command
from Config import getCommandName, getSetting
import re

DEVICES_WITHOUT_VOLUME_CONTROL = ["Tablet", "Smartphone"]


class SetVolume(Command):
    previousIncreaseCharacters = 0
    previousDecreaseCharacters = 0
    currentVolume = 0

    def __init__(self, spotify):
        super().__init__(getCommandName("SET_VOLUME_COMMAND"), spotify)

    def Match(self, query: str):
        if(self.spotify.current_playback()["device"]["type"] in DEVICES_WITHOUT_VOLUME_CONTROL):
            return [("", "Volume cannot be controlled on the current device", "Spotify", 100, 100, {})]

        query = query.strip(" ")
        returnOptions = []
        if(query.isnumeric() and len(query) > 0):
            returnOptions = self.setVolumeByValue(query)
        elif(re.search('^[' + getSetting("DECREASE_VOLUME_CHARACTER") + getSetting("INCREASE_VOLUME_CHARACTER") + ']*$', query)):

            decreaseCharacters = query.count(
                getSetting("DECREASE_VOLUME_CHARACTER"))
            increaseCharacters = query.count(
                getSetting("INCREASE_VOLUME_CHARACTER"))
            if(decreaseCharacters == 0 and increaseCharacters == 1) or (decreaseCharacters == 1 and increaseCharacters == 0):
                SetVolume.currentVolume = self.spotify.current_playback()[
                    "device"]["volume_percent"]
            if(decreaseCharacters > SetVolume.previousDecreaseCharacters):
                SetVolume.currentVolume = SetVolume.currentVolume - int(getSetting("VOLUME_STEP")) * abs(decreaseCharacters - SetVolume.previousDecreaseCharacters)
            elif(increaseCharacters > SetVolume.previousIncreaseCharacters):
                SetVolume.currentVolume = SetVolume.currentVolume + int(getSetting("VOLUME_STEP")) * abs(increaseCharacters - SetVolume.previousIncreaseCharacters)
            elif(decreaseCharacters < SetVolume.previousDecreaseCharacters):
                SetVolume.currentVolume = SetVolume.currentVolume + int(getSetting("VOLUME_STEP")) * abs(decreaseCharacters - SetVolume.previousDecreaseCharacters)
            elif(increaseCharacters < SetVolume.previousIncreaseCharacters):
                SetVolume.currentVolume = SetVolume.currentVolume - int(getSetting("VOLUME_STEP")) * abs(increaseCharacters - SetVolume.previousIncreaseCharacters)
            SetVolume.previousDecreaseCharacters = decreaseCharacters
            SetVolume.previousIncreaseCharacters = increaseCharacters
            if SetVolume.currentVolume < 0:
                SetVolume.currentVolume = 0
                returnOptions = [(" ", "Min volume reached!", "Spotify", 100, 100, {})]
            elif SetVolume.currentVolume > 100:
                SetVolume.currentVolume = 100
                returnOptions = [(" ", "Max volume reached!", "Spotify", 100, 100, {})]
            else:
                returnOptions = [(" ", "Volume has been set to: " + str(SetVolume.currentVolume) + "%", "Spotify", 100, 100, {})]
            self.spotify.volume(SetVolume.currentVolume)
        else:
            returnOptions = self.setVolumeByChoice()
        return returnOptions

    def Run(self, data: str):
        self.spotify.volume(int(data))

    def setVolumeByValue(self, query):
        volume = int(query)
        if(volume < 0 or volume > 100):
            return [(" ", "Volume has to be between 1 and 100%", "Spotify", 100, 100, {})]
        else:
            return [(self.command + " " + str(volume), "Increase volume with " + str(volume) + "%", "Spotify", 100, 100, {})]

    def setVolumeByChoice(self):
        return [
            (self.command + " 10", "Set volume to 10%",
             "Spotify", 100, 100, {}),
            (self.command + " 25", "Set volume to 25%",
             "Spotify", 100, 80, {}),
            (self.command + " 50", "Set volume to 50%",
             "Spotify", 100, 60, {}),
            (self.command + " 100", "Set volume to 100%", "Spotify", 100, 40, {})]
