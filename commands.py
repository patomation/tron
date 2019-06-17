# Command Argument Functions
from modules import backup, duplicate

def run(args):

    if args.which == 'file':
        if args.d:
            duplicate.file(args.d)
        elif args.b:
            backup.file(args.b)

    elif args.which == 'job':
        print 'job script'
        print args.a
        # if args.a:
        #     job.applied(args.a)
