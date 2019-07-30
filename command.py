# Command Argument Functions
from modules import backup, duplicate, Json

config = Json.importer('/config.json')

from commands import job, xlaunch

def run(args):
    print args.which + ' command activated:'

    if args.which == 'file':
        if args.d:
            duplicate.file(args.d)
        elif args.b:
            backup.file(args.b)

    elif args.which == 'job_applied':
        job.applied(
            company=args.c,
            aplicationType=args.t,
            position=args.p,
            url=args.url,
            email=args.e,
            location=args.l,
            notes=args.n)
    elif args.which == 'xlaunch':
        xlaunch.start(config)
