from modules import duplicate, backup

def options():
    return {
        'help':'this is a test command',
        'args': [{
            'name':'-d',
            'help':'Duplicate [PATH]',
            'action':'store',
            'required':False
        },{
            'name':'-b',
            'help':'Backup [PATH]',
            'action':'store',
            'required':False
        }]
    }
def run(args):
    if args.d != None and args.b != None:
        print 'Please use only one command'
        exit()

    if args.d != None:
        print 'duplicate'
        duplicate.file(args.d)

    elif args.b != None:
        print 'backup'
        backup.file(args.b)
