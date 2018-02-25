from file_handler import get_years_sheet

def average_crime_per_year(sheet, row_num):
    return sheet.cell(row_num, 3).value + sheet.cell(row_num, 13).value

def fq_answer(avg1995, avg2013):
    print(avg1995)
    print(avg2013)

    if avg1995 > avg2013:
        return "Crime decreased since 1995 until 2013 by " + str(round(100 - avg2013 * 100 / avg1995, 2)) + "%"
    else:
        return "Crime increased since 1995 until 2013 by " + str(round(100 - avg1995 * 100 / avg2013, 2)) + "%"

sheet = get_years_sheet()

print(fq_answer(average_crime_per_year(sheet, 4), average_crime_per_year(sheet, 23)))