import requests
import shutil
import openpyxl
import xlrd
from openpyxl.workbook import Workbook as openpyxlWorkbook


def download_file(url):
    split = url.split("/")
    file_name = split[len(split) - 1]
    print(file_name)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


# download_file("https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/"
#                   "table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls")

def average_crime_per_year(sheet, row_num):
    return sheet.cell(row_num, 3).value + sheet.cell(row_num, 13).value


def answer(avg1995, avg2013):
    print(avg1995)
    print(avg2013)

    if avg1995 > avg2013:
        return "Crime decresed since 1995 until 2013 by " + str(round(100 - avg2013 * 100 / avg1995, 2)) + "%"
    else:
        return "Crime increased since 1995 until 2013 by " + str(round(100 - avg1995 * 100 / avg2013, 2)) + "%"


def first_question():
    xlsBook = xlrd.open_workbook('./output.xls')
    sheet = xlsBook.sheet_by_index(0)

    print(answer(average_crime_per_year(sheet, 4), average_crime_per_year(sheet, 23)))


first_question()
