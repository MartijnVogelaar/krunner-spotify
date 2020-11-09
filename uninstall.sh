
#!/bin/bash

# Exit if something fails
set -e

rm ~/.local/share/kservices5/plasma-runner-KRunnerSpotify.desktop
rm ~/.local/share/dbus-1/services/org.kde.KRunnerSpotify.service
rm ~/.config/KRunner-Spotify/KRunner-Spotify.config

#Deletes cache from the default CACHE_PATH, has to be manually deleted if changed
rm ~/.cache/KRunnerSpotify/.cache
kquitapp5 krunner