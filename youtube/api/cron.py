import argparse
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
QUERY = 'cricket'
MAX_RESULT = 20

def get_key(para):
    API_KEYS = os.environ['API_KEY'].split(',')
    if para == 'default':
        return API_KEYS[0]
    else:
        index = (API_KEYS.index(para)+1)%len(API_KEYS)
        return API_KEYS[index]
    


def youtube_pull(key = 'default'):
    try:
        if key == 'default':
            api_key = get_key('default')
        else:
            api_key = get_key(key)
        
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = api_key)
        search_response = youtube.search().list(
            q = QUERY,
            part = 'id,snippet',
            maxResults = MAX_RESULT,
            type = 'video'
        ).execute()
        for i in search_response.items():
            print(i)
        videos = []
    
        for search_result in search_response.get('items', []):
            videos.append('%s %s %s %s (%s)' % (search_result['snippet']['title'], search_result['snippet']['publishedAt'], search_result['snippet']['thumbnails']['default']['url'],
            search_result['snippet']['description'], search_result['id']['videoId']))
    except HttpError as e:
        if e.resp.status == 403:
            youtube_pull(api_key)
        if e.resp.status == 400:
            print("Invalid api key")
    
    print('Videos:\n', '\n'.join(videos), '\n')
