import os
import scraper

main():
    scraper.scrape({
        'location': 'Portland, OR',
        'search': 'Software Engineer',
        'output': os.getcwd() + '/myJobSearch.xlsx'
    })

if __name__ == "__main__":
    main()
