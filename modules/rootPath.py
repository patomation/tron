# GETS Root FOLDER PATH
import os

def get():
    realPath = os.path.realpath(__file__) #File Path
    dirnamePath = os.path.dirname(realPath) # Folder Path of file using this
    parrentPath = os.path.dirname(dirnamePath) # up one directory path
    return parrentPath
