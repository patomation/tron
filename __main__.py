from modules import startScreen, arguments

# Command Argument Functions
from modules import backup, duplicate

def main():
    startScreen.show();

    arguments.add({
        'name':'file',
        'help': 'File Managerment Tool',
        'args':{
            '-d': 'Duplicate [PATH]',
            '-b': 'Backup [PATH]'
        }
    })
    arguments.add({
        'name':'file',
        'help': 'File Managerment Tool',
        'args':{
            '-d': 'Duplicate [PATH]',
            '-b': 'Backup [PATH]'
        }
    })

    arguments.add({
        'name':'scrape',
        'help': 'Scrape',
        'args':{
            '--gs': 'Google Search Results [URL]'
        },
        'do': 'stuff'
    })


    args = arguments.get()

    if args.which == 'file':
        if args.d:
            duplicate.file(args.d)
        elif args.b:
            backup.file(args.b)


if __name__ == "__main__":
    main()
