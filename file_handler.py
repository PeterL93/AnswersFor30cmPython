import os.path
import requests
import shutil
import xlrd

def download_file(file_name, url):
    split = url.split("/")
    og_file_name = split[len(split) - 1]
    print("Downloaded " + file_name)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(og_file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
            os.rename("./" + og_file_name, "./" + file_name)

def get_years_sheet():
    years_sheet_file_name = "years_sheet.xls"
    if not os.path.exists("./" + years_sheet_file_name):
        download_file(years_sheet_file_name, "https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/"
        "table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls/output.xls")
    return xlrd.open_workbook("./" + years_sheet_file_name).sheet_by_index(0)

def get_locations_sheet():
    locations_sheet_file_name = "locations_sheet.xls"
    if not os.path.exists("./" + locations_sheet_file_name):
        download_file(locations_sheet_file_name, "https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls")
    return xlrd.open_workbook("./" + locations_sheet_file_name, formatting_info=True).sheet_by_index(0)
