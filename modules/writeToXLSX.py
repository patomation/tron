import json
import xlsxwriter



def write(posts, fileName):

    # Make excell file
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet()
    # Write Titles
    worksheet.write('A1', 'Title')
    worksheet.write('B1', 'Score')
    worksheet.write('C1', 'Comments')
    worksheet.write('D1', 'Date')
    worksheet.write('E1', 'Link')

    # Yes in another for loop because I want to keep functionality separate
    rownumber = 2
    for post in posts:
        worksheet.write('A'+str(rownumber), post['title'] )
        worksheet.write('B'+str(rownumber), post['score'] )
        worksheet.write('C'+str(rownumber), post['comments'] )
        worksheet.write('D'+str(rownumber), post['date'] )
        worksheet.write('E'+str(rownumber), post['url'] )
        rownumber += 1


    workbook.close()























#
