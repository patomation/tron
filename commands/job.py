from modules import today, excel, Json

config = Json.importer('/config.json')

def applied(company, aplicationType, position, url, email='', location='', notes=''):
    print 'You applied for a job'
    aplicationType if aplicationType else 'online';
    excel.append(
        path=config['job']['aplicationLog'],
        data=[
            company, # Company
            today.date(), # Date
            aplicationType, # Applied Check off
            '', # Status
            position, # Position Applied For
            url, # Application url
            email,
            location,
            notes
        ])
