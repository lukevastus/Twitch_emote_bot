import json
import urllib.request

raw = urllib.request.urlopen("https://twitchemotes.com/api_cache/v2/global.json")
data = json.loads(raw.read())
emote_lib = {}
omitted = ["SSSsss", "Kappa"]

print("Updating emote database...")
for key,value in data["emotes"].items():
    if key in omitted:
        continue
    emote_lib.update({key: value["image_id"]})

# print(emote_lib)

