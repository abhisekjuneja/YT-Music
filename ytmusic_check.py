from ytmusicapi import YTMusic
import pprint

pp = pprint.PrettyPrinter(indent=4)

YTMusicObj = YTMusic("authentication_headers.json")


likedPlaylistItems = YTMusicObj.get_liked_songs()
for likedItem in likedPlaylistItems["tracks"]:
	pp.pprint(f"{likedItem['title']} by {likedItem['artists']}")

# searchResults = YTMusicObj.search(query = "Trampoline")
# pp.pprint(searchResults)