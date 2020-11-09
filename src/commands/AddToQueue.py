from .Command import Command
from .ArtistSong import ArtistSong
from .Song import Song
from Config import getCommandName, getSetting

class AddToQueue(Command):
    def __init__(self, spotify):
        super().__init__(getCommandName("ADD_TO_QUEUE_COMMAND"), spotify)

    def Match(self, query: str):
        arguments = ""
        if(" " in query):
            command, arguments = query.split(" ",1)
        else:
            command = query
            
        try:
            results = self.executeCommand(command).Match(arguments)
            for i in range(0,len(results)):
                tempResult = list(results[i])
                tempResult[0] = self.command + " " + tempResult[0]
                results[i] = tuple(tempResult)
            return results
        except RuntimeError:
            return [("", "Invalid command", "Spotify", 100, 100, {})]
        
    def Run(self, data: str):
        if("track" in data):
            self.spotify.add_to_queue(uri=data)

    def executeCommand(self, command: str):
        if(getSetting("CASE_SENSITIVE") == "False"):
            command = command.upper()
        if(command == getCommandName("PLAY_SONG_COMMAND")):
            return Song(self.spotify)
        elif(command == getCommandName("PLAY_SONG_BY_ARTIST_COMMAND")):
            return ArtistSong(self.spotify)
        raise RuntimeError("Incorrect command")
