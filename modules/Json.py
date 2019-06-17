import json
import rootPath

def importer(path):
    return json.load(open(rootPath.get()+path))
