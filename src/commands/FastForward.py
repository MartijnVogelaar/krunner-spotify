from .Command import Command
from Config import getCommandName


class FastForward(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("FAST_FORWARD_COMMAND"), spotify)

    def Match(self, query: str):
        query = query.strip(" ")
        if(query.isnumeric()):
            seconds = int(query)
            return [(self.command + " " + str(seconds), "Fastforward " + str(seconds) + " seconds.", "Spotify", 100, 100, {})]
        else:
            return [(self.command + " 5", "Fastforward 5 seconds.", "Spotify", 100, 100, {}),
                    (self.command + " 15", "Fastforward 15 seconds.", "Spotify", 90, 100, {}),
                    (self.command + " 60", "Fastforward 1 minute", "Spotify", 80, 100, {}),
                    (self.command + " 300", "Fastforward 5 minutes", "Spotify", 70, 100, {}),
                    (self.command + " 600", "Fastforward 10 minutes", "Spotify", 60, 100, {})]

    def Run(self, data: str):
        self.spotify.seek_track(self.spotify.current_playback()[
                                "progress_ms"] + (int(data) * 1000))
