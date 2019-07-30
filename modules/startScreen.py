from os import system
import platform


def clear():
    if platform.system() == 'Windows':
        _ = system('cls')
    else:
        _ = system('clear')

def show():
    # Clear Screen
    clear()

    # Display Obligitory Branding Message
    print '_________ _______  _______  _       '
    print '\__   __/(  ____ )(  ___  )( (    /|'
    print '   ) (   | (    )|| (   ) ||  \  ( |'
    print '   | |   | (____)|| |   | ||   \ | |'
    print '   | |   |     __)| |   | || (\ \) |'
    print '   | |   | (\ (   | |   | || | \   |'
    print '   | |   | ) \ \__| (___) || )  \  |'
    print '   )_(   |/   \__/(_______)|/    )_)'
    print ''
    print '         [ Atomate your job ]'
    print ''
