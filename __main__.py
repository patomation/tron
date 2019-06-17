from modules import startScreen, Json, parser
arguments = Json.importer('/arguments.json')
import command

def main():
    startScreen.show();

    # Add all arguments from arguments config file
    parser.addArguments(arguments)

    command.run( parser.getArgs() )



if __name__ == "__main__":
    main()
