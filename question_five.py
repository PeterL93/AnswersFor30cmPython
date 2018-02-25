from file_handler import get_years_sheet
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def year(sheet, row_num):
    return sheet.cell(row_num, 0).value

def violent_crimes(sheet, row_num):
    return sheet.cell(row_num, 3).value

def property_crimes(sheet, row_num):
    return sheet.cell(row_num, 13).value

sheet = get_years_sheet()

crimes1995 = np.array([violent_crimes(sheet, 4), property_crimes(sheet, 4)])
crimes2013 = np.array([violent_crimes(sheet, 23), property_crimes(sheet, 23)])

print(crimes1995)
print(crimes2013)

fig = plt.figure()
x = np.array([0, 1])
my_xticks = ["Violent Crimes", "Property Crimes"]
plt.xticks(x, my_xticks)
num_crimes1995 = plt.bar(my_xticks, crimes1995, color='r')
num_crimes2013 = plt.bar(my_xticks, crimes2013, color='b')
plt.legend((num_crimes1995[0], num_crimes2013[0]), ("1995", "2013"))
plt.title("Average Crimes commited ")
plt.xlabel("Type of crimes")
plt.ylabel("Average crime rate")

fig.savefig('Question5.png')

print("Picture saved as + Question5.png")