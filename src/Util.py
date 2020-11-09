import re


def parseSearchQuery(query):
    page = 0
    query = query.lstrip(" ")
    if(re.findall("p\d+$", query)):
        query, page = query.rsplit("p", 1)
    page = int(page)
    if(page < 1):
        page = 1
    return query, page


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
