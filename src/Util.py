import re


def parseSearchQuery(query):
    query = query.lstrip(" ")
    if (query == ""):
        return query, 1
    page = 0
    result = list(filter(None, re.split(r" (p\d+$)", query)))
    if(len(result) == 1):
        return result[0], 1
    else:
        page = int(result[1][1:])
        return result[0], page


def parseArtists(results):
    parsedResults = []

    for artist in results['items']:
        parsedResults.append(
            (artist["uri"], artist['name'], "Spotify", 100, 100, {}))
    if(not parsedResults):
        parsedResults.append(
            ("", "No artists found!", "Spotify", 100, 100, {}))
    return parsedResults


def parseTracks(results):
    parsedResults = []
    for track in results["tracks"]["items"]:
        track_details = (track["name"] + " - " +
                         track["album"]["artists"][0]["name"])
        parsedResults.append(
            (track["uri"], track_details, "Spotify", 100, 100, {}))
    if(not parsedResults):
        parsedResults.append(
            ("", "No tracks found!", "Spotify", 100, 100, {}))
    return parsedResults


def parsePlaylists(playlists):
    parsedResults = []
    for playlist in playlists["items"]:
        parsedResults.append(
            (playlist["uri"], playlist["name"], "Spotify", 100, 100, {}))
    if(not parsedResults):
        parsedResults.append(
            ("", "No playlists found!", "Spotify", 100, 100, {}))
    return parsedResults
