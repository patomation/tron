import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

# PROPS
# - name - String: sub parser name
# - args - Object: Key name Value help description
def add(props):
    # Create new sub parser
    newSubParser = subparser.add_parser(props['name'])
    # Set which arg so we can find it later
    newSubParser.set_defaults(which=props['name'])
    for key in props['args']:
        newSubParser.add_argument(key, help=props['args'][key])

def get():
    return parser.parse_args()
