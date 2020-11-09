# KRunner-Spotify

This plugin allows you to easily control [Spotify](https://www.spotify.com/) using [KRunner](https://github.com/KDE/krunner). The plugin uses [Spotipy](https://github.com/plamere/spotipy) to interact with the [Spotify Web API](https://developer.spotify.com/documentation/web-api/). Using only a handful of words the user can control Spotify in a straightforward manner, even if Spotify does not run on the same device as KRunner is running. 


# Queries

The queries which can be entered are made out of the following parts:

* [Main-Command](#Main-Commands) | **Required**
* [Sub-Command](#Sub-Commands)  | **Optional**

A `query` has to be started with a `main-command` and can thus only contain one `main-command`. Depending on the chosen `main-command` either nothing, a `sub-command` or argument(s) have to be supplied. If a `sub-command` has to be supplied this `sub-command` can require argument(s).

Examples:
```
$[Main-Command]
```

```
$[Main-Command] $[Arg1] $[Arg2]
```

```
$[Main-Command] $[Sub-Command] $[Arg1] $[Arg2]
```

To be clear, a `main-command` can **either** have a `sub-command` or have one or more argument(s). Due to the fact that the `sub-command` can have argument(s), a `query` can in fact contain a `main-command` , `sub-command` and one or more argument(s).
The following is thus **not allowed**:
```
$[Main-Command] $[Arg1] $[Sub-Command] $[Arg1] $[Arg2]
```
<br/><br/>

<!-- ----------------------------------------------------------------- --> 

# **Main-Commands**

## **Add**
The [add](##add) command can be used to add a track to the queue. To be able to use the add command a `sub-command` has to be supplied. The supported `sub-commands` for the [add](##add) command are the following:
* [song by artist](##Artist)
* [song](##song)
</br></br>

## **Examples**:</br>
Add the song "Mockingbird" to the queue
```
Add song mockingbird
```
Add a song by "Eminem" 
```
Add artist Eminem 
```
</br></br>

## **Decrease volume**
The [DecVol](##Decrease-Volume) command can be used to decrease the volume of the playback device.
There are two ways of using the [DecVol](##Decrease-Volume) command:

* Entering the [DecVol](##Decrease-Volume) command produces the following results:
  * Decrease volume with 10%
  * Decrease volume with 25%
  * Decrease volume with 50%
  * Decrease volume with 100%
* Entering the [DecVol](##Decrease-Volume) command with a value x (0 <= x <= 100) as argument will create a result which allows you to decrease the volume with x%.
</br></br>

## **EditConfig**
The [EditConfig](##EditConfig) command allows you to easily open the configuration file in the graphical editor chosen specified in the config file.
```
Note: the changes in the configuration do not apply untill:
   • the plugin is restarted
   • execution of the ReloadConfig command.
```
</br>


## **Increase volume**
The [IncVol](##Increase-Volume) command can be used to increase the volume of the playback device.
There are two ways of using the [IncVol](##Increase-Volume) command:

* Entering the [IncVol](##Increase-Volume) command produces the following results:
  * Increase volume with 10%
  * Increase volume with 25%
  * Increase volume with 50%
  * Increase volume with 100%
* Entering the [IncVol](##Increase-Volume) command with a value `x` (0 <= `x` <= 100) as argument will create a result which allows you to increase the volume with `x%`.
</br></br>


## **Login**
The `Login` command can be used to authorize the plugin to control your Spotify via the WebAPI. After entering this command the Spotify `Login` screen is automatically opened in your preferred browser.

```
Note: If the user is not yet logged in, any `main-command` will act as if the `Login` command is entered. 
```
</br>

## **Logout**
The `Logout` command can be used to log out. On execution of the `Logout` command the .cache file containing the authentication token is deleted.
</br></br>


## **Next**
The `Next` command can be used to skip a track.
</br></br>

## **Previous**
The `Previous` command can be used to play the last played a track.
</br></br>

## **Pause**
The `Pause` command can be used to pause the current track.
</br></br>


## **Play**
The `Play` command can be used to play for example a playlist or track. To be able to use the `Play` command a `sub-command` has to be supplied. The supported `subcommands` are the following:
* `Play` [featured](##Featured)
* `Play` [myplaylist](##myplaylist)
* `Play` [playlist](##playlist)
* `Play` [artist](##artist)
* `Play` [song](##song)

## **Examples**:</br>
Play the song "Mockingbird"
```
Play song mockingbird
```
Play a song by "Eminem" 
```
Play artist Eminem 
```
</br>

## **Resume**
The `Resume` command can be used to resume/start the current track.
</br></br>


## **Start Spotify**
The `Spotify` can be used to start Spotify in your default browser.
</br></br>

## **TrackInfo**
The `TrackInfo` command can be used to retrieve information about the current track playing. The info being shown
depends on the type of track being played. The following two types with the following info are available:
 * Music, show title, artist, progress and duration. 
 * Episode of a show, shows title of the show, name of the episode, progress and duration. 
</br></br>


<!-- ----------------------------------------------------------------- --> 


# Sub-Commands

## Featured
The `featured` `sub-command` can be used in combination with the `Play` command. When the feature `sub-command` is supplied after the `Play` command featured playlists are shown. The featured `sub-command` takes one optional argument:

* Page number, showing pages more results by entering: p{$_pagenumber}. (**Optional**)  


### **Examples**:</br>
The following `query` can be used to show the featured playlists. After selecting a playlist it will be played. 
```
Play featured
```
The following `query` can be used to show the second page with featured playlists. After selecting a playlist it will be played. 
```
Play featured p2
```
</br>

## My playlist
The `myplaylist` `sub-command` can be used in combination with the `Play` command. When the `myplaylist` `sub-command` is supplied after the `Play` command your playlists are shown. The `myplaylist` `sub-command` takes one optional argument:

* Page number, showing pages more results by entering: p{$_pagenumber}. (**Optional**)  


### **Examples**:</br>
The following `query` can be used to show your playlists. After selecting a playlist it will be played.
```
Play myplaylist
```
The following `query` can be used to show the second page with your playlists. After selecting a playlist it will be played. 
```
Play myplaylist p2
```
</br>

## Playlist
The `playlist` `sub-command` can be used in combination with the `Play` command. The playlist `sub-command` takes two arguments:

* Search term, title of the playlist which should be searched for. (**Required**)
* Page number, showing pages more results by entering: p{$_pagenumber}. (**Optional**)  


### **Examples**:</br>
The following command can be used to search for a playlist which is named: "2pac". After selecting a playlist it will be played.
```
Play playlist 2pac
```
The following command can be used to search for a playlist which is named: "2pac" and show the second page. After selecting a playlist it will be played.
```
Play playlist 2pac p2
```
</br>

## Artist
The `artist` `sub-command` can be used in combination with both the `Play` as `Add` command. The `artist` `sub-command` takes two arguments:

* Search term, name of the artist which should be searched for. (**Required**)
* Page number, showing pages more results by entering: p{$_pagenumber}. (**Optional**)  

### **Examples**:</br>
The following command can be used to search for a song by: "Eminem". After selecting the song it will be played.
```
Play artist Eminem
```
The following command can be used to search for a song by: "Eminem" and will show the second page. After selecting the song it will be added to the queue.
```
Add artist Eminem p2
```
</br>


## Song

The `song` `sub-command` can be used inc ombination with both the `Play` as `Add` command. The artist `sub-command` takes two arguments:

* Search term, name of the song which should be searched for. (**Required**)
* Page number, showing pages more results by entering: p{$_pagenumber}. (**Optional**)  

### **Examples**:</br>
The following command can be used to search for a song named: "Mockingbird". After selecting the song it will be played.
```
Play song Mockingbird
```
The following command can be used to search for a song named: "Stan" and will show the second page. After selecting the song it will be added to the queue.
```
Add song Stan p2
```


# Config file

The config file is split in two parts:
* Settings, containing general settings, path etc
* Names of the commands

Editing the config file can be done in two different ways:
* Open and edit the config file located in "***~/.config/KRunner-Spotify/***" in your favorite text editor.
* Execute the `EditConfig` command.

After editing the config file, it has to be (re)loaded into the plugin, this can be done by either reloading the entire plugin, or executing the `ReloadConfig` command.

## Settings
* **MAX_RESULTS** defines the number of results shown at once
* **CACHE_PATH** is the path which will be used to save the acces_token.
* **CASE_SENSITIVE** defines whether commands are CaSe SEnSiTIVe
* **CONFIG_EDITOR** defines which text editor will be opened when entering the EditConfig command.


## Commandnames
In the Command names part of the config file the exact commands needed to activatie the funtionaliteits can be defined. 

```
Note that as of now commands cannot contain spaces!
```
