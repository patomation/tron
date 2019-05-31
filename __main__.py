import argparse
import os
import scraper

def main():
    parser = argparse.ArgumentParser(description='Bulk Saving Of Job Posts')
    parser.add_argument('-q',
                    help='Search Term Query')
    parser.add_argument('-l',
                    help='Location')
    parser.add_argument('-o',
                    help='Output location')
    parser.add_argument('--json',
                    help='Export Json File')
    parser.add_argument('--xlsx',
                    help='Export Excel File')

    args = parser.parse_args()

    # print(args.accumulate(args.integers))
    if args.l == None:
        print "Must include location with: -l 'location'"
        exit
    if args.q == None:
        print "Must include search term with: -q 'job title'"
        exit

    if( args.q != None and args.l != None ):
        print 'make this stuff happen'
        output = ''
        if (args.o == None):
            fileName = args.l.replace(' ','-').replace(',','')+'-'+args.q.replace(' ','-')
            output = os.getcwd() + '/' + fileName + '.xlsx'
        else:
            output = args.o
        scraper.scrape({
            'location': args.l,
            'search': args.q,
            'output': output
        })

if __name__ == "__main__":
    main()
