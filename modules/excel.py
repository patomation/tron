import json
import xlsxwriter
import string

alphabet = str(string.ascii_uppercase)

def write(props):
    print 'WRITE EXCEL-----------------------------'

    # Make excell file
    workbook = xlsxwriter.Workbook(props['fileName'])
    worksheet = workbook.add_worksheet()
    # Write Titles
    for letter in alphabet:
        if letter in props['colums']:
            worksheet.write( letter+'1', props['colums'][letter].upper() )
        else:
            break

    # Yes in another for loop because I want to keep functionality separate
    rownumber = 2
    for item in props['items']:
        for letter in alphabet:
            if letter in props['colums']:
                # key exists in item
                if props['colums'][letter] in item:
                    worksheet.write(letter+str(rownumber), item[props['colums'][letter]] )
                # Write Blank
                else:
                    worksheet.write(' ')
            else:
                break
        rownumber += 1

    print 'close....'
    workbook.close()














#
