from file_handler import get_years_sheet

sheet = get_years_sheet()


class CrimeResult:
    most_crimes = 0
    name = ''
    year = ''


def compare_crimes_amount_and_get_result(amount_to_compare, result):
    if result.most_crimes < amount_to_compare:
        result.most_crimes = amount_to_compare
        result.year = int(sheet.cell(row_number, 0).value)
        return True
    return False


most_crime_a_year = CrimeResult()
for row_number in range(4, 24):
    crime_in_a_year = int(sheet.cell(row_number, 2).value + sheet.cell(row_number, 12).value)
    compare_crimes_amount_and_get_result(crime_in_a_year, most_crime_a_year)

print("Year with most crime was: " + str(most_crime_a_year.year) + " with a total of " + str(
    most_crime_a_year.most_crimes) + " various crimes commited.")

most_frequent_crime = CrimeResult()


def go_through_crime_amounts_and_compare(row_number, result, range_of_cells):
    for col_number in range_of_cells:
        crime_amount = int(sheet.cell(row_number, col_number).value)
        if compare_crimes_amount_and_get_result(crime_amount, result):
            result.name = sheet.cell(3, col_number).value.strip('\n')


for row_number in range(4, 24):
    go_through_crime_amounts_and_compare(row_number, most_frequent_crime, range(4, 12, 2))
    go_through_crime_amounts_and_compare(row_number, most_frequent_crime, range(14, 20, 2))

print("Most frequent crime was " + str(most_frequent_crime.name) +
      " with a total of " + str(most_frequent_crime.most_crimes) +
      " occurrences in the year " + str(most_frequent_crime.year) + ".")
