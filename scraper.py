from pprint import pprint
from os import system
import sys


# My Modules
from modules import html, queryString, excel

def scrape(props):
    # Clear Screen
    _ = system('clear')

    # Display Obligitory Branding Message
    print " _____           _               _    _____                                "
    print "|_   _|         | |             | |  / ____|                               "
    print "  | |  _ __   __| | ___  ___  __| | | (___   ___ _ __ __ _ _ __   ___ _ __ "
    print "  | | | '_ \ / _` |/ _ \/ _ \/ _` |  \___ \ / __| '__/ _` | '_ \ / _ \ '__|"
    print " _| |_| | | | (_| |  __/  __/ (_| |  ____) | (__| | | (_| | |_) |  __/ |   "
    print "|_____|_| |_|\__,_|\___|\___|\__,_| |_____/ \___|_|  \__,_| .__/ \___|_|   "
    print " "
    print " "
    print " "
    print "==========================================================================="
    print " "
    print " "

    # Abstracts checking if element exists to prevent erors
    def text (element):
        string = ''
        if element != 'None':
            if hasattr(element, 'text'):
                string = element.text.replace('  ','')
        return string

    url='https://www.indeed.com/jobs?q='+props['search'].replace(' ','%20')+'&l='+props['location'].replace(' ','%20').replace(',','%2C')
    page = html.parse(url)

    totalJobsText = text( page.find('div', { 'id':'searchCount'}) )
    if totalJobsText == '':
        print 'NO RESULTS FOUND'
        return

    pages = int(totalJobsText.split('of ')[1].replace(' jobs','').replace(',',''))

    jobs = []
    currentPage = 0
    while currentPage <= pages:
        print str(currentPage)+' of '+ str(pages)

        page = html.parse(url+'&start='+str(currentPage))

        for job in page.findAll('div', { 'class':'jobsearch-SerpJobCard'}):
            title = text( job.find('a', {'class': 'jobtitle'}) )
            company = text( job.find('span', {'class': 'company'}) )
            location = text( job.find('span', {'class': 'location'}) )

            jobPostUrl = 'https://www.indeed.com'+job.find('a', {'class': 'jobtitle'}).get('href')
            queryStrings = queryString.parse( jobPostUrl )
            if 'jk' in queryStrings:
                applyUrl = 'https://www.indeed.com/rc/clk?jk='+queryStrings['jk']+'&from=vj&pos=bottom'
            else:
                applyUrl = ''

            date = text( job.find('span', {'class': 'date'}) )

            jobs.append({
                'title'      : title,
                'company'    : company,
                'location'   : location,
                'jobPostUrl' : jobPostUrl,
                'applyUrl'   : applyUrl,
                'date'       : date,
            })

        currentPage += 10
    print '-----------------------------------------------------------------'
    print 'Finished Scraping'
    print '-----------------------------------------------------------------'
    # print jobs
    print '...Processing Output Files....'
    excel.write({
        'columns':{
            'A' : {'label':'company'   ,'width':30},
            'B' : {'label':'applied'   ,'width': 5},
            'C' : {'label':'title'     ,'width':30},
            'D' : {'label':'location'  ,'width':10},
            'E' : {'label':'date'      ,'width':10},
            'F' : {'label':'applyUrl'  ,'width':30},
            'G' : {'label':'jobPostUrl','width':30},
        },
        'items':jobs,
        'fileName': props['output']
    })
