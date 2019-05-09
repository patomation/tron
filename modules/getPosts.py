import requests

import cleanMyData


def getPosts(subReddit, searchQuery):
    print 'working on getting posts from ' + subReddit + ' with question: ' + searchQuery
    # Fake header
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    searchQuery = searchQuery.replace(' ', '%20')

    sort = 'relivance'
    pages=10

    query = r'https://www.reddit.com/r/'+subReddit+'/search.json?q=title:%22'+searchQuery+'%22&restrict_sr=1&sort='+sort+'&count=25'

    posts = []
    after = ''

    page = 1
    while page <= pages:
        print 'working on page '+str(page)+' of '+str(pages)
        data = requests.get(query+after, headers=headers).json()

        # Clean data
        cleanPosts = cleanMyData.clean(data)

        # store clean posts
        posts.extend(cleanPosts)

        page += 1

        # Set next after or set next page
        if data['data']['after'] != None:
            after = '&after='+data['data']['after']
        else:
            # Do not run again no more paginations
            print 'There were no more pages'
            break

    return posts
