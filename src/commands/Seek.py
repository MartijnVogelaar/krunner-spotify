from .Command import Command
from Config import getCommandName


class Seek(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("SEEK_COMMAND"), spotify)

    def Match(self, query: str):
        query = query.strip(" ")
        time = query.split(":")
        if all(x.isnumeric() for x in time):
            if len(time) == 1:
                return [(self.command + " " + time[0], "Seek: " + time[0] + " sec", "Spotify", 100, 100, {})]
            if len(time) == 2:
                return [(self.command + " " + str(60*int(time[0]) + int(time[1])), "Seek: " + time[0] + " min " + time[1] + " sec", "Spotify", 100, 100, {})]
            if len(time) == 3:
                return [(self.command + " " + str(60*60 * int(time[0]) + 60*int(time[1]) + int(time[2])), "Seek: " + time[0] + " hr " + time[1] + " min " + time[2] + " sec", "Spotify", 100, 100, {})]
        else:
            return [("", "Invalid input.", "Spotify", 100, 100, {})]

    def Run(self, data: str):
        self.spotify.seek_track(int(data) * 1000)
