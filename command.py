# Command Argument Functions
from modules import gatekeeper, backup, duplicate

from commands import job

def run(args):

    if args.which == 'file':
        if args.d:
            duplicate.file(args.d)
        elif args.b:
            backup.file(args.b)

    elif args.which == 'job_applied':
        job.applied(
            company=args.c,
            position=args.p,
            url=args.url)
