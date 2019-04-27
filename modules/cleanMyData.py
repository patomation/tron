import json
from pprint import pprint

import timeStampToDate

# Make reddits json pritty and
# ... only keep the data we care about
def clean(dirtyData):
    posts = []
    for item in dirtyData['data']['children']:
        # print item['data']['title']
        post = {
            'title': item['data']['title']  ,
            'comments': int(item['data']['num_comments']),
            'score': int(item['data']['score']),
            'date': timeStampToDate.convert(item['data']['created_utc']),
            'url': str(item['data']['url'])
        }
        posts.append(post)
    return posts






















#
