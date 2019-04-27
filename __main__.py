from pprint import pprint
import requests
import json
from bs4 import BeautifulSoup
import sys
import numpy as np
import os

# My Modules
from modules import cleanMyData
from modules import writeToXLSX

def main():
    # Fake header
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    subReddit = 'r/webdev'
    searchQuery = 'how%20do%20I' # How Do I
    sort = 'relivance'
    pages=10

    query = 'https://www.reddit.com/'+subReddit+'/search.json?q='+searchQuery+'&restrict_sr=1&sort='+sort

    posts = []
    after = ''

    page = 1
    while page <= pages:
        print 'working on page '+str(page)+' of '+str(pages)
        data = requests.get(query+after, headers=headers).json()

        # Set next after or set next page
        after = data['data']['after']

        # Clean data
        cleanPosts = cleanMyData.clean(data)

        # store clean posts
        posts.extend(cleanPosts)
        print len(cleanPosts)
        page += 1

    # Create target Directory
    dirName = './output'
    try:
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    except:
        print("Directory " , dirName ,  " already exists")

    # Make json file
    fileName = dirName+"/redditposts.json"
    with open(fileName, 'w') as outfile:
        json.dump(posts, outfile)

    # Make xlsx file
    writeToXLSX.write(posts, dirName+'/redditposts.xlsx')

    # Let me know when your done
    print 'Done BRO'

if __name__ == "__main__":
    main()
