import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()

# Checks daya key value or uses default
def check(data, key, default):
    if key in data:
        value = data[key]
    else:
        value = default
    return value

def addSubArgument(name, help, args):
    # Create sub parser
    newSubParser = subparser.add_parser(
        name,
        help=help)
    newSubParser.set_defaults(which=name)

    # Add sub parser flags
    for arg in args:
        newSubParser.add_argument(
            arg['name'],
            help=arg['help'],
            action=check(data=arg,key='action',default='store'),
            required=check(data=arg,key='required',default=False)
        )

def addArgument(name, help, action, required):
    parser.add_argument(
        name,
        help=help,
        action=action,
        required=required
    )

def parse_args():
    return parser.parse_args()
