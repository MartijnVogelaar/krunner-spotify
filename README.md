# KRunner-Spotify

This plugin allows you to easily control [Spotify](https://www.spotify.com/) using [KRunner](https://github.com/KDE/krunner). The plugin uses [Spotipy](https://github.com/plamere/spotipy) to interact with the [Spotify Web API](https://developer.spotify.com/documentation/web-api/). Using only a handful of words the user can control Spotify in a straightforward manner, even if Spotify does not run on the same device as KRunner is running on. Whether you are playing Spotify on your phone, Chromecast(Audio), Smart TV or anyother device, you are able to control it using this plugin!  

# Dependencies
In order to run the project the following software needs to be installed:
* [Python3](https://www.python.org/download/releases/3.0/)
* [Pip3](https://pip.pypa.io/en/stable/)
* [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/) - minimum version of 2.14.0

<br/>

# Install
After installing all dependencies listed above, the following steps are needed to finish the installation:
1. Clone the repo
```sh
git clone https://github.com/MartijnVogelaar/krunner-spotify
```
2. Install
```sh
sh install.sh
```
<br/><br/>
# Uninstall
In order to uninstall the plugin the following has to be done:
1. Navigate to the repo
```sh
cd /path/to/repo
```
2. Install
```sh
sh uninstall.sh
```
<br/>

## Functionalities

The KRunner-Spotify plugin has a wide range of functionalities including:
* Adding songs to the queue
* Increasing/Decreasing the volume
* Pause/Resume a track
* Play next/previous track
* Play a song/playlist
* Search for songs, artists, playlists and your playlists
* View the info of the current track


## Usage
See [`USAGE.md`](USAGE.md) for an extensive guide.

## Future implementations:
* Control your own playlists
    * Create
    * Delete
    * Rename
    * Add (current) song to playlist
* Search and play album by name
* Search and play album by artists name
* Play an artist besides just searching for songs by artist.


## License
Distributed under the GPL-3.0 License. See [`LICENSE`](LICENSE) for more information.


## Contact

Martijn Vogelaar - Martijn.j.Vogelaar@outlook.com

Project Link: [GitHub](https://github.com/MartijnVogelaar/krunner-spotify)
