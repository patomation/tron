import os, importlib

def all(folderPath):
    modules = {}

    scriptPath = os.path.dirname(os.path.realpath(__file__))

    for root, dirs, files in os.walk( os.path.join(scriptPath, folderPath) ):
        for fname in files:
            if fname.endswith('.py') and fname != '__init__.py':
                fname = fname.replace('.py', '')
                module = importlib.import_module(folderPath+'.'+fname)
                # Save moudle
                modules[fname] = module
    return modules
