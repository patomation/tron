import argparse
from modules import startScreen, parser
import importFolder

def main():
    startScreen.show();

    # Import functions and apply thier args
    functions = importFolder.all('functions')
    for key in functions:
        options = functions[key].options()
        parser.addSubArgument(
            name=key,
            help=options['help'],
            args=options['args']
        )

    # Get all args
    args = parser.parse_args()
    # Runn sub arg function
    functions[args.which].run(args);


if __name__ == "__main__":
    main()
