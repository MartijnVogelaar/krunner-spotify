import configparser
import os

CONFIG_FILE_LOCATION = os.path.expanduser(
    "~") + "/.config/KRunner-Spotify/KRunner-Spotify.config"


def loadConfig():
    global config
    config.read(CONFIG_FILE_LOCATION)
    config["Settings"]["CACHE_PATH"] = os.path.expanduser(
        config["Settings"]["CACHE_PATH"])


def getCommandName(commandName):
    try:
        if(config["Settings"]["CASE_SENSITIVE"] == "False"):
            return config["CommandNames"][commandName].upper()
        else:
            return config["CommandNames"][commandName]
    except Exception as e:
        print("Command: " + str(e) + "not found!")


def getSetting(settingName):
    try:
        return config["Settings"][settingName]
    except Exception as e:
        print("Setting: " + str(e) + "not found!")


config = configparser.ConfigParser()
loadConfig()
