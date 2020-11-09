from .Command import Command
from Config import getCommandName, getSetting, CONFIG_FILE_LOCATION
import os


class EditConfig(Command):
    def __init__(self, spotify):
        self.command = getCommandName("EDIT_CONFIG_COMMAND")

    def Match(self, query: str):
        if(os.path.isfile(getSetting("CONFIG_EDITOR"))):
            return [(self.command, "Edit configuration", "Spotify", 100, 100, {}), ]
        else:
            return [(self.command, "Given editor: " + getSetting("CONFIG_EDITOR") + " not found!", "Spotify", 100, 100, {}), ]

    def Run(self, data: str):
        os.system(getSetting("CONFIG_EDITOR") +
                  " " + CONFIG_FILE_LOCATION + "&")
