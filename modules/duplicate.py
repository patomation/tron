# Duplicates a file
from shutil import copyfile
import ntpath

def getNextNumber(oldNumber):
    print oldNumber
    newInteger = int(oldNumber) + 1
    newInegerString = str(newInteger)

    newNumber = '000'

    if   ( len(newInegerString) == 1 ):
        newNumber = '00' + newInegerString
    elif ( len(newInegerString) == 2 ):
        newNumber = '0' + newInegerString
    elif ( len(newInegerString) == 3 ):
        newNumber = newInegerString
    return newNumber

def file(sourcePath):
    print 'duplicating file...'
    path, file = ntpath.split(sourcePath)
    fileName, extension = file.split('.')

    # check if file name has _00n in the back
    version = fileName.split('_')[-1]
    # is version number
    if ( len(version) == 3 ):
        newVersion = getNextNumber('000')
        fileName = fileName.replace(version, newVersion)
    # is not version number
    else:
        fileName = fileName + '_000'

    destinationPath = path +'/'+ fileName +'.'+ extension

    print sourcePath
    print destinationPath
    copyfile(sourcePath, destinationPath)
