import os
from os.path import expanduser
home = expanduser("~")

def get(path):
    return path.replace('~',home)
