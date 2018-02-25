from file_handler import get_locations_sheet
import pprint
import numpy as np
import matplotlib.pyplot as plt

def populations_list(merged_cells):
    populations_list = list()
    for merged_cell in merged_cells:
        sum = 0
        for row in range(merged_cell[0], merged_cell[1]):
            sum += sheet.cell(row, 2).value
        populations_list.append(sum)
    return populations_list

sheet = get_locations_sheet()
pp = pprint.PrettyPrinter(indent=4)

merged_cells = sorted(sheet.merged_cells, key=lambda merged_cell: merged_cell[0])

# print(sheet.cell(4, 0))
print(len(merged_cells) - 11)
print(merged_cells[len(merged_cells) - 11])

for x in range(len(merged_cells) - 12, len(merged_cells) - 2):
    del merged_cells[x]

# pp.pprint(merged_cells)

ind = np.arange(len(merged_cells))

# fig, ax = plt.subplots()

# pp.pprint(populations_list(merged_cells))