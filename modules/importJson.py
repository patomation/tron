import json
import rootPath

def load(path):
    return json.load(open(rootPath.get()+path))
