import os, subprocess

from modules import expandUserPath

def file(path):
    filePath = expandUserPath.get(path)
    # win 32
    # os.startfile(path)
    # Mac
    # subprocess.call('open filename')
    # Linux
    # Dosn't work
    subprocess.call('xdg-open '+str(filePath))
