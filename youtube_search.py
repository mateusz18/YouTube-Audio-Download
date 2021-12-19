import os

from googleapiclient.discovery import build


def get_url(titles, urls):
    while True:
        if titles.empty():
            continue
        title = titles.get()
        api_key = os.environ.get('yt_api_key')  # here you need to paste your own api key for YouTube Data API v3
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            order='relevance',
            q=f'{title}',
            part='snippet',
            type='vide',
            regionCode='PL',  # PL is a region code that can be changed or removed
            maxResults=1
        )
        response = request.execute()
        url = 'https://www.youtube.com/watch?v=' + response['items'][0]['id']['videoId']
        urls.put(url)
