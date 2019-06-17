from modules import today, excel, Json

config = Json.importer('/config.json')

def applied(company, position, url):
    print 'You applied for a job'
    excel.append(
        path=config['job']['aplicationLog'],
        data=[
            company, # Company
            today.date(), # Date
            'X', # Applied Check off
            '', # Status
            position, # Position Applied For
            url # Application url
        ])
