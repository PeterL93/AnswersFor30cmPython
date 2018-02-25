from file_handler import get_locations_sheet
import pprint

def population_sum()

sheet = get_locations_sheet()
pp = pprint.PrettyPrinter(indent=4)

merged_cells = sorted(sheet.merged_cells, key=lambda merged_cell: merged_cell[0])

pp.pprint(merged_cells)
print(sheet.cell(4, 0))

# for merged_cell in merged_cells:
