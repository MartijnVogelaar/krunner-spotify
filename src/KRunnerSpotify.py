from commands import Commands
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyPKCE
from Config import getCommandName, getSetting
import dbus.service
import spotipy
import os

DBusGMainLoop(set_as_default=True)

objpath = "/KRunnerSpotify"
iface = "org.kde.krunner1"


class Runner(dbus.service.Object):
    def __init__(self):
        dbus.service.Object.__init__(self, dbus.service.BusName(
            "org.kde.KRunnerSpotify", dbus.SessionBus()), objpath)
        os.makedirs(os.path.dirname(getSetting("CACHE_PATH")), exist_ok=True)
        self.auth_manager = SpotifyPKCE(client_id=getSetting("CLIENT_ID"),
                                        cache_path=getSetting("CACHE_PATH"),
                                        redirect_uri=getSetting(
                                            "REDIRECT_URI"),
                                        scope=getSetting("ACCES_SCOPE"))
        self.spotify = spotipy.Spotify(auth_manager=self.auth_manager)

    @dbus.service.method(iface, in_signature="s", out_signature="a(sssida{sv})")
    def Match(self, query: str):
        arguments = ""
        if(" " in query):
            command, arguments = query.split(" ", 1)
        else:
            command = query
        try:
            if(getSetting("CASE_SENSITIVE") == "False"):
                command = command.upper()
            return Commands.executeCommand(command, self.spotify).Match(arguments)
        except RuntimeError as e:
            if(str(e) == "Not logged in!"):
                return [(getCommandName("LOGIN_COMMAND"), "Not logged in, click to login", "Spotify", 100, 100, {})]
            elif(str(e) == "No playback device available!"):
                return [(getCommandName("START_SPOTIFY_COMMAND"), "No playback device available, click to open Spotify!", "Spotify", 100, 100, {})]

    @dbus.service.method(iface, in_signature="ss")
    def Run(self, data: str, action_id: str):
        command = data
        if(" " in data):
            command, data = data.split(" ", 1)
        else:
            data = ""
        try:
            Commands.executeCommand(command, self.spotify).Run(data)
        except RuntimeError as e:
            print(e)


runner = Runner()
loop = GLib.MainLoop()
loop.run()
