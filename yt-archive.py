#!/bin/python3

import urllib.request as request
import json
import shutil
import os
from dotenv import load_dotenv
from yt_dlp import YoutubeDL
# from email import header

def get_all_video_in_channel(channel_id):
  api_key = os.environ['YT_API_KEY']

  base_video_url = 'https://www.youtube.com/watch?v='
  base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

  first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)

  video_links = []
  url = first_url
  while True:
    inp = request.urlopen(url)
    resp = json.load(inp)

    for i in resp['items']:
      if i['id']['kind'] == "youtube#video":
        video_links.append(base_video_url + i['id']['videoId'])

    try:
      next_page_token = resp['nextPageToken']
      url = first_url + '&pageToken={}'.format(next_page_token)
    except:
      break
  return video_links

def main():
  load_dotenv()

  channels = os.environ['CHANNELS'].split(',')

  for channel_id in channels:
    # Gets most recent video from creator
    # videos = get_all_video_in_channel('channel_id') # hard coded for now
    
    # Downloads the videos
    with YoutubeDL() as ydl:
      ydl.download('https://www.youtube.com/watch?v=D9SFvNpBTBM')

    # Moves downloaded videos to media destination
    dl_videos = [f for f in os.listdir() if '.mp4' in f.lower()]
    
    # Creates the save directory if it doesn't exist
    if not os.path.exists(os.environ['DL_PATH']):
      os.makedirs(os.environ['DL_PATH'])
    
    # Moves all downloaded videos
    for dl_video in dl_videos:
      new_path = os.environ['DL_PATH'] + '/' + dl_video
      shutil.move(dl_video, new_path)

if __name__=="__main__":
  main()