from .Command import Command
from Config import getCommandName, getSetting

class Repeat(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("REPEAT_COMMAND"), spotify)

    def Match(self, query: str):
        if(getSetting("CASE_SENSITIVE") == "False"):
            query = query.lower()
        if(query in ["track","context","off"]):
            return [(self.command + " " + query, "Set repeat mode to: " + query + ".", "Spotify", 100, 100, {})]
        else:
            return [(self.command + " off", "Set repeat mode to: off.", "Spotify", 100, 100, {}),
                    (self.command + " context", "Set repeat mode to: context.", "Spotify", 100, 100, {}),
                    (self.command + " track", "Set repeat mode to: track.", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        self.spotify.repeat(data)
