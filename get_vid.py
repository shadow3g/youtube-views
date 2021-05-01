#!/usr/bin/env python3
#pip3 install google-api-python-client
import googleapiclient.discovery

#Voidreaper
#playlist_id = "UUT1wNkriwrFPEnl0eCW6bzw"
#Benjamin
playlist_id = "UUCU-BLPu_rNfRiMR1XqvMbQ"

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyB90q9Hhr8HwmEolu6UcSeRUKVAS190Vuc")

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 500
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

#print(f"total: {len(playlist_items)}")
#print(playlist_items)

import json
with open('data.json', 'w') as outfile:
    json.dump(playlist_items, outfile)
with open('data.json') as f:
  data = json.load(f)
for i in range (0, len(data)):
    print("https://youtu.be/" + data[i]['snippet']['resourceId']['videoId'])
    # print(data[i]['snippet']['resourceId']['videoId'])
