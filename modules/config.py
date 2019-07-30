import os.path
from os import path

from modules import Json

scriptPath = os.path.dirname(os.path.realpath(__file__))
configPath = path.abspath(os.path.join( scriptPath, '..', 'config.json' ))
def get(option):
    if path.exists( configPath ) == False:
        exit()
    else:
        return Json.importer(configPath)[option]

def save(options):
    Json.write(configPath, options)
