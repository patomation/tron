# Duplicates a file
from shutil import copyfile
import ntpath

def file(sourcePath):
    print 'creating backup copy...'
    path, file = ntpath.split(sourcePath)
    fileName, extension = file.split('.')

    destinationPath = path +'/'+ fileName +'_backup'+'.'+ extension
    print sourcePath
    print destinationPath
    # copyfile(sourcePath, destinationPath)
