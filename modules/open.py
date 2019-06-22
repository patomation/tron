import os, subprocess

from modules import expandUserPath

def file(path):
    print path
    filePath = expandUserPath.get(path)
    print filePath
    # win 32
    # os.startfile(path)
    # Mac
    # subprocess.call('open filename')
    # Linux
    # Dosn't work
    print 'xdg-open '+str(filePath)
    subprocess.call('xdg-open '+str(filePath))
