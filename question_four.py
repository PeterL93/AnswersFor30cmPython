from file_handler import get_locations_sheet
import pprint
import numpy as np
import matplotlib.pyplot as plt


def states_list(merged_cells):
    states_list = list()
    for merged_cell in merged_cells:
        if not sheet.cell(merged_cell[0], 0).value == '':
            states_list.append(sheet.cell(merged_cell[0], 0).value)
    del states_list[len(states_list) - 1]
    del states_list[len(states_list) - 2]
    del states_list[len(states_list) - 3]
    return states_list


def populations_list(merged_cells):
    populations_list = list()
    for merged_cell in merged_cells:
        sum = 0
        for row in range(merged_cell[0], merged_cell[1]):
            if type(sheet.cell(row, 2).value).__name__ == 'float' and not sheet.cell(row, 2).value == 0:
                sum += sheet.cell(row, 2).value
        populations_list.append(sum / 1000)
    del populations_list[len(populations_list) - 1]
    del populations_list[len(populations_list) - 2]
    del populations_list[len(populations_list) - 3]
    return populations_list


def violent_crimes_list(merged_cells):
    violent_crimes_list = list()
    for merged_cell in merged_cells:
        sum = 0
        for row in range(merged_cell[0], merged_cell[1]):
            if type(sheet.cell(row, 3).value).__name__ == 'float' and not sheet.cell(row, 3).value == 0:
                sum += sheet.cell(row, 3).value
        violent_crimes_list.append(sum)
    del violent_crimes_list[len(violent_crimes_list) - 1]
    del violent_crimes_list[len(violent_crimes_list) - 2]
    del violent_crimes_list[len(violent_crimes_list) - 3]
    return violent_crimes_list


def property_crimes_list(merged_cells):
    property_crimes_list = list()
    for merged_cell in merged_cells:
        sum = 0
        for row in range(merged_cell[0], merged_cell[1]):
            if type(sheet.cell(row, 3).value).__name__ == 'float' and not sheet.cell(row, 3).value == 0:
                sum += sheet.cell(row, 3).value
        property_crimes_list.append(sum)
    del property_crimes_list[len(property_crimes_list) - 1]
    del property_crimes_list[len(property_crimes_list) - 2]
    del property_crimes_list[len(property_crimes_list) - 3]
    return property_crimes_list


sheet = get_locations_sheet()
pp = pprint.PrettyPrinter(indent=4)

sorted_merged_cells = sorted(sheet.merged_cells, key=lambda merged_cell: merged_cell[0])

x = 50
while not x == 48:
    del sorted_merged_cells[x]
    x -= 1

# pp.pprint(sorted_merged_cells)

states_list = states_list(sorted_merged_cells)
populations_list = populations_list(sorted_merged_cells)
violent_crimes_list = violent_crimes_list(sorted_merged_cells)
property_crimes_list = property_crimes_list(sorted_merged_cells)

# print(len(states_list))
# print(len(populations_list))

# pp.pprint(states_list)
# pp.pprint(populations_list)

ind = np.arange(len(states_list))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 9))

population_plots = ax.bar(ind, populations_list, width, color="b")
violent_crimes_plots = ax.bar(ind + width, violent_crimes_list, width, color="r")
property_crimes_plots = ax.bar(ind + width * 2, property_crimes_list, width, color="g")

ax.set_ylabel("Populations (thousands)")
ax.set_title("Populations and Violent Crimes Chart")
ax.set_xticks(ind)
ax.set_xticklabels(states_list)
# ax.legend((population_plots[0]), ('Population'))

for label in ax.get_xticklabels():
    label.set_rotation(70)

plt.show()

fig_name = "question_four.png"

fig.savefig(fig_name)
