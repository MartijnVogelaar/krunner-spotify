from .AddToQueue import AddToQueue
from .CurrentTrackInfo import CurrentTrackInfo
from .DecreaseVolume import DecreaseVolume
from .EditConfig import EditConfig
from .IncreaseVolume import IncreaseVolume
from .Login import Login
from .Logout import Logout
from .Next import Next
from .Pause import Pause
from .Play import Play
from .Previous import Previous
from .ReloadConfig import ReloadConfig
from .Repeat import Repeat
from .Resume import Resume
from .StartSpotify import StartSpotify
from .Shuffle import Shuffle
from .FastForward import FastForward
from .Rewind import Rewind
from .Seek import Seek
from .SetVolume import SetVolume
from Config import getCommandName


def executeCommand(command, spotify):
    if(command == getCommandName("NEXT_COMMAND")):
        return Next(spotify)
    elif(command == getCommandName("PREVIOUS_COMMAND")):
        return Previous(spotify)
    elif(command == getCommandName("PAUSE_COMMAND")):
        return Pause(spotify)
    elif(command == getCommandName("RESUME_COMMAND")):
        return Resume(spotify)
    elif(command == getCommandName("DECREASE_VOLUME_COMMAND")):
        return DecreaseVolume(spotify)
    elif(command == getCommandName("INCREASE_VOLUME_COMMAND")):
        return IncreaseVolume(spotify)
    elif(command == getCommandName("PLAY_COMMAND")):
        return Play(spotify)
    elif(command == getCommandName("ADD_TO_QUEUE_COMMAND")):
        return AddToQueue(spotify)
    elif(command == getCommandName("START_SPOTIFY_COMMAND")):
        return StartSpotify(spotify)
    elif(command == getCommandName("LOGOUT_COMMAND")):
        return Logout(spotify)
    elif(command == getCommandName("LOGIN_COMMAND")):
        return Login(spotify)
    elif(command == getCommandName("CURRENT_TRACK_INFO_COMMAND")):
        return CurrentTrackInfo(spotify)
    elif(command == getCommandName("RELOAD_CONFIG_COMMAND")):
        return ReloadConfig(spotify)
    elif(command == getCommandName("EDIT_CONFIG_COMMAND")):
        return EditConfig(spotify)
    elif(command == getCommandName("SHUFFLE_COMMAND")):
        return Shuffle(spotify)
    elif(command == getCommandName("REPEAT_COMMAND")):
        return Repeat(spotify)
    elif(command == getCommandName("FAST_FORWARD_COMMAND")):
        return FastForward(spotify)
    elif(command == getCommandName("REWIND_COMMAND")):
        return Rewind(spotify)
    elif(command == getCommandName("SEEK_COMMAND")):
        return Seek(spotify)
    elif(command == getCommandName("SET_VOLUME_COMMAND")):
        return SetVolume(spotify)