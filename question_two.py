from file_handler import get_years_sheet
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def average_murder_per_year(sheet, row_num):
    return sheet.cell(row_num, 5).value

def average_rape_per_year(sheet, row_num):
    return sheet.cell(row_num, 7).value

def average_robbery_per_year(sheet, row_num):
    return sheet.cell(row_num, 9).value

def average_aggravated_assault_per_year(sheet, row_num):
    return sheet.cell(row_num, 11).value

def average_burglary_per_year(sheet, row_num):
    return sheet.cell(row_num, 15).value

def average_larceny_per_year(sheet, row_num):
    return sheet.cell(row_num, 17).value

def average_vehicle_theft_per_year(sheet, row_num):
    return sheet.cell(row_num, 19).value

sheet = get_years_sheet()

crimes_1995 = np.array(
    [average_murder_per_year(sheet, 4), average_rape_per_year(sheet, 4), average_robbery_per_year(sheet, 4),
     average_aggravated_assault_per_year(sheet, 4), average_burglary_per_year(sheet, 4),
     average_larceny_per_year(sheet, 4), average_vehicle_theft_per_year(sheet, 4)])
crimes_2013 = np.array(
    [average_murder_per_year(sheet, 23), average_rape_per_year(sheet, 23), average_robbery_per_year(sheet, 23),
     average_aggravated_assault_per_year(sheet, 23), average_burglary_per_year(sheet, 23),
     average_larceny_per_year(sheet, 23), average_vehicle_theft_per_year(sheet, 23)])

print(crimes_1995)
print(crimes_2013)

fig = plt.figure()
x = np.array([0, 1, 2, 3, 4, 5, 6])
my_xticks = ["Murder", "Rape", "Robbery", "Assault", "Burglary", "Larceny", "GTA"]
plt.xticks(x, my_xticks)
_1995 = plt.bar(my_xticks, crimes_1995, color='r')
_2013 = plt.bar(my_xticks, crimes_2013, color='b')
plt.legend((_1995[0], _2013[0]), ("1995", "2013"))
plt.title("Crime Rates")
plt.xlabel("Crime Type")
plt.ylabel("Rate")

fig.savefig('test.png')

print("Check the new png file created in the directory")