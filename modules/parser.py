import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers()
# PROPS
# - arguments - dict
def addArguments(arguments):
    for name in arguments:
        argument = arguments[name]

        # Create sub parser
        newSubParser = subparser.add_parser(name)
        newSubParser.set_defaults(which=name)

        # Add sub parser flags
        for argName in argument['args']:
            arg = argument['args'][argName]
            # Help text is required
            help = arg['help']
            # Action store value by default
            # store_true and Store_false would let you use a flag wihtout a value...
            if 'action' in arg:
                action = arg['action']
            else:
                action = 'store'
            newSubParser.add_argument(
                argName,
                help=help,
                action=action )

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
