import json
import os

import excel

def write(items, fileName):
    # Create target Directory
    dirName = './output'
    try:
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created .")
    except:
        print("Directory " , dirName ,  " already exists, so I wont make a new one.")

    # Make json file
    # print 'Writing json file'
    # filePath = dirName+'/'+fileName+'.json'
    # with open(filePath, 'w') as outfile:
    #     json.dump(items, outfile)

    # Make xlsx file
    print 'Writing exell file'
    excel.write({
        'colums':{
            'A' : 'company'   ,
            'B' : 'applied'   ,
            'C' : 'title'     ,
            'D' : 'location'  ,
            'E' : 'applyUrl'  ,
            'F' : 'jobPostUrl',
        },
        'items':items,
        'fileName': dirName+'/'+fileName+'.xlsx'
    })
