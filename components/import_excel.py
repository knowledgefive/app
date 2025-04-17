# accessing excel
import os, sys
import pandas as pd
from openpyxl import load_workbook

def open_excel(workbook_path:str, target_worksheet_name:str):
    '''
    a function for reading an excel document

    PARAMETERS
    ----------
    workbook_path : str
    target_worksheet_name : str

    RETURN 
    ------
    dataframe

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

    # load target worksheet into a dataframe
    target_worksheet = pd.read_excel(workbook_path, sheet_name=target_worksheet_name)

    # return target worksheet if it not empty
    return None if target_worksheet.empty else target_worksheet

if __name__ == "__main__":

    # TESTING
    workbook_path = "data.xlsx"
    worksheet = "shopping"
    dataframe = open_excel(workbook_path, worksheet)
    print(f"test result\n{dataframe}")