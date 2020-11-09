#!/bin/bash

# Exit if something fails
set -e

mkdir -p ~/.local/share/kservices5/
mkdir -p ~/.local/share/dbus-1/services/


mkdir -p ~/.config/KRunner-Spotify

cp KRunner-Spotify.config ~/.config/KRunner-Spotify/
cp plasma-runner-KRunnerSpotify.desktop ~/.local/share/kservices5/
sed "s|%{PROJECTDIR}/KRunnerSpotify.py|${PWD}/src/KRunnerSpotify.py|" "org.kde.KRunnerSpotify.service" > ~/.local/share/dbus-1/services/org.kde.KRunnerSpotify.service

kquitapp5 krunner