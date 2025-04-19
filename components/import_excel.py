# interacting with an excel workbook in python
# import modules
import os, sys
import pandas as pd
from openpyxl import load_workbook

# a function to load excel into a pandas dataframe
# dataframes are often used to manipulate data 
def open_excel_workbook(workbook_path:str, target_worksheet_name:str):
    '''
    a function for reading an excel document

    PARAMETERS
    ----------
    workbook_path : str - path to excel workbook
    target_worksheet_name : str - excel worksheet name

    RETURN 
    ------
    dataframe : pd.Dataframe - pandas dataframe

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
    print(f"workbook {workbook_path} found with {worksheet} worksheets")

    # check target worksheet exists
    if target_worksheet_name not in worksheets:
        error_message = f"{target_worksheet_name} not found in worksheet list {worksheets} for document {workbook_path}"
        raise ValueError(error_message)

    # load target worksheet into a dataframe
    target_worksheet = pd.read_excel(workbook_path, sheet_name=target_worksheet_name)

    # return target worksheet if it not empty
    return None if target_worksheet.empty else target_worksheet

if __name__ == "__main__":

    # a test to turn the worksheet 'shopping" from the workbook 'data.xlsx' into a dataframe
    workbook_path = "data.xlsx"
    worksheet = "shopping"
    dataframe = open_excel_workbook(workbook_path, worksheet)
    print(f"dataframe\n{dataframe}")

    # an example of filtering the dataframe
    filtered_dataframe = dataframe[dataframe['item'] == 'orange']
    print(f"filtered dataframe\n{filtered_dataframe}")