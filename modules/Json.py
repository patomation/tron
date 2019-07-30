import json

def importer(path):
    return json.load(open(path))

def write(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
