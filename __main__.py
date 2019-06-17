from modules import startScreen, importJson, parser
arguments = importJson.load('/arguments.json')
import commands

def main():
    startScreen.show();

    # Add all arguments from arguments config file
    parser.addArguments(arguments)

    commands.run( parser.getArgs() )



if __name__ == "__main__":
    main()
