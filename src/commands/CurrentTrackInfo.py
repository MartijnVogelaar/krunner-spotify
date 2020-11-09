from .Command import Command
from Config import getCommandName
from datetime import timedelta
import time


class CurrentTrackInfo(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("CURRENT_TRACK_INFO_COMMAND"), spotify)

    def Match(self, query: str):
        playbackDetails = self.spotify.currently_playing(
            additional_types="episode")
        if(playbackDetails["item"]["type"] == "track"):
            trackName = playbackDetails["item"]["name"]
            trackArtist = playbackDetails["item"]["artists"][0]["name"]
            progress_s = int(playbackDetails["progress_ms"] / 1000)
            duration_s = int(playbackDetails["item"]["duration_ms"] / 1000)
            return [("", "Title: " + trackName, "Spotify", 100, 100, {}),
                    ("", "Artist: " + trackArtist, "Spotify", 100, 0.5, {}),
                    ("", "Progress: " + self.secondsToTime(progress_s) + " / " + self.secondsToTime(duration_s), "Spotify", 100, 0.0, {})]
        elif(playbackDetails["item"]["type"] == "episode"):
            showName = playbackDetails["item"]["show"]["name"]
            episodeName = playbackDetails["item"]["name"]
            progress_s = int(playbackDetails["progress_ms"] / 1000)
            duration_s = int(playbackDetails["item"]["duration_ms"] / 1000)
            return [("", "Show name: " + showName, "Spotify", 100, 100, {}),
                    ("", "Episode name: " + episodeName, "Spotify", 100, 0.5, {}),
                    ("", "Progress: " + self.secondsToTime(progress_s) + " / " + self.secondsToTime(duration_s), "Spotify", 100, 0.0, {})]

    def Run(self, data: str):
        return NotImplementedError

    def secondsToTime(self, seconds):
        format = "%H:%M:%S" if seconds > 3600 else "%M:%S"
        return time.strftime(format, time.gmtime(seconds))
