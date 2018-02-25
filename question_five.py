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

crimes1995 = (violent_crimes(sheet, 4), property_crimes(sheet, 4))
crimes2013 = (violent_crimes(sheet, 23), property_crimes(sheet, 23))

print(crimes1995)
print(crimes2013)

fig = plt.figure()

ind = np.arange(2)

num_crimes1995 = plt.bar(ind, crimes1995, color='r')
num_crimes2013 = plt.bar(ind, crimes2013, color='b')

plt.xticks(ind, ('Violent Crimes', 'Property Crimes'))

plt.legend((num_crimes1995[0], num_crimes2013[0]), ("1995", "2013"))
plt.title("Average Crimes commited")
plt.xlabel("Type of crimes")
plt.ylabel("Average crime rate")

fig_name = "question_five.png"

fig.savefig(fig_name)

print("Picture saved as " + fig_name)