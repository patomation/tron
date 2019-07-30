from modules import today, excel, config

def options():
    return {
        'help':'Job Helper',
        'args': [{
            'name':'-a',
            'help':'Logg applied for job',
            'action':'store_true',
            'required':False
        }]
    }

def run(args):

    # Job Applied
    if args.a == True:

        companyName=''
        aplicationType='online'
        position='Front End'
        url=''
        email=''
        location=''
        notes=''

        while True:
            companyName = raw_input("Company Name [{}]: ".format(companyName) ) or companyName
            aplicationType = raw_input("Application Type [{}]: ".format(aplicationType) ) or aplicationType
            position = raw_input("Position Applied For [{}]: ".format(position) ) or position
            url = raw_input("URL [{}]: ".format(url) ) or url
            email = raw_input("Email [{}]: ".format(email) ) or email
            location = raw_input("Location [{}]: ".format(location) ) or location
            notes = raw_input("Notes [{}]: ".format(notes) ) or notes
            print('')
            print('companyName:', companyName)
            print('aplicationType:', aplicationType)
            print('position:', position)
            print('url:', url)
            print('email:', email)
            print('location:', location)
            print('notes:', notes)
            print('')

            ok = raw_input("is this ok? [y/n] :") or "y"

            if ok == 'y' or ok == 'Y' or ok == 'Yes' or ok == 'YES' or ok == '':

                excel.append(
                    path=config.get('jobApplicationLog'),
                    data=[
                        companyName, # Company
                        today.date(), # Date
                        aplicationType, # Applied Check off
                        '', # Status
                        position, # Position Applied For
                        url, # Application url
                        email,
                        location,
                        notes
                    ])
                break



















#
