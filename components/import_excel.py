# accessing excel
import os, sys
from openpyxl import load_workbook

def open_excel(workbook_path:str, target_worksheet_name:str):
    '''
    a function for reading an excel document
    '''

    # check excel file exists
    if not os.path.isfile(workbook_path):
        error_message = f"{workbook_path} not found"
        raise FileNotFoundError(error_message)

    # load excel workbook as an object
    workbook = load_workbook(filename=workbook_path)

    # check worksheets
    worksheets = workbook.sheetnames

    if len(worksheets) == 0:
        error_message = f"{workbook_path} is empty"
        raise ValueError(error_message)

    # output results to terminal
    print(f"workbook {workbook_path} found with {len(worksheets)} worksheets")

    # check target worksheet exists
    if target_worksheet_name not in worksheets:
        error_message = f"{target_worksheet_name} not found in {workbook_path}"
        raise ValueError(error_message)

    # load worksheet object
    target_worksheet = workbook[target_worksheet_name]

    # loop through target worksheet
    for row in target_worksheet.iter_rows():

        row_values = []

        for cell in row:
            row_values.append(cell.value)

        print(f"worksheet row - {row_values}")

if __name__ == "__main__":

    # TESTING
    workbook_path = "data.xlsx"
    worksheet = "shopping"
    open_excel(workbook_path, worksheet)