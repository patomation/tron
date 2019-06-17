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
    for argName in args:
        arg = args[argName]
        newSubParser.add_argument(
            argName,
            help=arg['help'],
            action=check(data=arg,key='action',default='store'),
            required=check(data=arg,key='required',default='required')
        )

def addArgument(name, help, action, required):
    parser.add_argument(
        name,
        help=help,
        action=action,
        required=required
    )

# PROPS
# - arguments - dict
def addArguments(arguments):
    for name in arguments:
        argument = arguments[name]
        # Flagged arguments
        if name[:1] == '-':
            addArgument(
                name=name,
                help=argument['help'],
                action=check(data=argument, key='action', default=True),
                required=check(data=argument, key='required', default=False)
            )
        # Sub arguments
        else:
            addSubArgument(
                name=name,
                help=argument['help'],
                args=argument['args'])




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

def getArgs():
    return parser.parse_args()
