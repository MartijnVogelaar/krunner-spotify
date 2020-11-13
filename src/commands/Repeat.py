from .Command import Command
from Config import getCommandName

class Repeat(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("REPEAT_COMMAND"), spotify)

    def Match(self, query: str):
        if(query in ["track","context","off"]):
            return [(self.command + " " + query, "Set repeat state to: " + query + ".", "Spotify", 100, 100, {})]
        else:
            return [(" " , "Invalid mode, repeat mode can be: track, context or off.", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        self.spotify.repeat(data)
