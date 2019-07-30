from modules import today, excel, config
import os

def options():
    return {
        'help':'Run Tron Setup',
        'args': []
    }

def run(args):
    print 'run setup function'
    print args

    jobApplicationLog = 'C:\Users\patrick\Google Drive\Resumes\_APPLICATION-LOG.xlsx'

    while True:
        jobApplicationLog = raw_input("jobApplicationLog Path [{}]: ".format(jobApplicationLog) ) or jobApplicationLog

        print ''
        print 'jobApplicationLog:', jobApplicationLog
        print ''

        ok = raw_input("is this ok? [y/n] :") or "y"

        if ok == 'y' or ok == 'Y' or ok == 'Yes' or ok == 'YES':
            print 'SAVE'
            config.save({
                'jobApplicationLog': os.path.join(jobApplicationLog)
            });
            break




















#