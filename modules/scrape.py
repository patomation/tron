# My Modules
import html, queryString, excel

# Abstracts checking if element exists to prevent erors
def text (element):
    string = ''
    if element != 'None':
        if hasattr(element, 'text'):
            # Get rid of spaces in front of text
            # TODO: Make better
            string = element.text.replace('  ','')
    return string

def scrape(props):

    page = html.parse(props['url'])

    data = {
        'company'  : text( page.find('h1', { 'class':'brand-text'}).a ),
        'date'     : 'today',
        'position' : text( page.find('div', { 'class':'job-header'}).h1 ),
        'status'   : 'applied',
        'website'  : props['url']
    }

    for key in data:
        print key + ': ' + data[key]
