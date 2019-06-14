import argparse
import sys

parser = argparse.ArgumentParser(description='TRON computer automator/ helper')

# Function storeage
functions = {}

def add(props):
    # Store functionz
    functions[props['arg'].replace('-','')] = props['function']

    parser.add_argument(
        props['arg'],
        help=props['help'])

def start():
    # Display help if no command given
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # For each stored function
    for key in functions:
        # Get argument value if any
        argValue = vars(args)[key]
        # If argument used find matching stored function
        if argValue:
            functions[key](argValue)
