from pprint import pprint
import json
from bs4 import BeautifulSoup
import sys
import os

# My Modules
from modules import writeToXLSX
from modules import getPosts

def main():

    subReddit = 'webdev'


    searchQueries = [
        'how do I',
        'How do you',
        'How can I',
        'I cant stand',
        'Im struggling with',
        'Can someone help',
        'Figure out',
        'Help me',
        'Tips',
        'Suggestions',
        'Suggest',
        'Biggest challenge',
        'Biggest challenges',
        'Hardest part',
        'Biggest struggle',
        'Struggle with'
    ]

    posts = []
    for searchQuery in searchQueries:
        posts.extend(getPosts.getPosts(subReddit, searchQuery))



    # Create target Directory
    dirName = './output'
    try:
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    except:
        print("Directory " , dirName ,  " already exists")

    # A file name using the subReddit

    fileName = subReddit+'-question-posts';

    # Make json file
    print 'Writing json file'
    filePath = dirName+'/'+fileName+'.json'
    with open(filePath, 'w') as outfile:
        json.dump(posts, outfile)

    # Make xlsx file
    print 'Writing exell file'
    writeToXLSX.write(posts, dirName+'/'+fileName+'.xlsx')

    # Let me know when your done
    print 'Done BRO'

if __name__ == "__main__":
    main()
