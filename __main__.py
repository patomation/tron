from modules import startScreen, arguments

# Command Argument Functions
from modules import backup, duplicate

def main():
    startScreen.show();

    arguments.add({
        'arg': '-b',
        'help': 'Backup [file location]',
        'function': backup.file
    })
    arguments.add({
        'arg': '-d',
        'help': 'Duplicate [file location]',
        'function': duplicate.file
    })

    arguments.start()

    print '----------------------------------'
    print ' D O N E'
    print '----------------------------------'
if __name__ == "__main__":
    main()
