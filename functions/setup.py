from modules import today, excel, config
import os

def options():
    return {
        'help':'Run Tron Setup',
        'args': []
    }

def run(args):

    jobApplicationLog = ''

    while True:
        jobApplicationLog = input("jobApplicationLog Path [{}]: ".format(jobApplicationLog) ) or jobApplicationLog

        print('')
        print('jobApplicationLog:', jobApplicationLog)
        print('')

        ok = input("is this ok? [y/n] :") or "y"

        if ok == 'y' or ok == 'Y' or ok == 'Yes' or ok == 'YES':
            config.save({
                'jobApplicationLog': os.path.join(jobApplicationLog)
            });
            break




















#
