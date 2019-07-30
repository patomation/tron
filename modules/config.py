import os.path
from os import path

from modules import Json

scriptPath = os.path.dirname(os.path.realpath(__file__))
configPath = path.abspath(os.path.join( scriptPath, '..', 'config.json' ))
def get(option):
    print 'get the config'
    if path.exists( configPath ) == False:
        print 'Config Not Created'
        print 'run: tron setup'
        exit()
    else:
        return Json.importer(configPath)[option]

def save(options):
    print 'make config'
    print options
    Json.write(configPath, options)
