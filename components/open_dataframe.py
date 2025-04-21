# making a simple choice window
# import FreeSimpleGUI module
import FreeSimpleGUI as sg  
import pandas as pd                  

sg.theme('Reddit')

def open_dataframe(dataframe, title:str):
    '''
    create the main GUI window
    '''

    # check if the parameter is a dataframe
    if not isinstance(dataframe, pd.DataFrame):
        error_message = f"dataframe parameter is not a dataframe"
        raise ValueError(error_message)
    
    # check if the dataframe is empty
    if dataframe.empty:
        error_message = f"dataframe is empty"
        raise ValueError(error_message)
    
    # check if the title is a string
    if not isinstance(title, str):
        error_message = f"title parameters {title} are not a string"
        raise ValueError(error_message)
    
    # check if the string is empty
    if len(title) == 0:
        error_message = f"title is empty"
        raise ValueError(error_message)

    # prepare table headings and values
    table_headings = list(dataframe.columns)
    table_values = dataframe.values.tolist()    

    # build GUI components
    table_title = sg.Text(title)
    table_element = sg.Table(values=table_values, headings=table_headings, max_col_width=20,
                             auto_size_columns=True,
                             display_row_numbers=True,
                             justification='center',
                             alternating_row_color='lightblue',
                             key='-GUI-TABLE-',
                             selected_row_colors='red on yellow',
                             enable_events=True, 
                             expand_x=True,
                             expand_y=True,
                             vertical_scroll_only=False,
                             tooltip='')
    
    table_close = sg.Button('Close', key='-GUI-CLOSE-')

    # set the layout of the window contents
    layout = [
        [table_title],
        [table_element],
        [table_close],
               ]

    # create the gui window
    window = sg.Window("Table", layout, resizable=False, finalize=True, element_justification='c')    

    while True:
        event, values = window.read()    
        if event == 'Exit' or event ==sg.WIN_CLOSED or event == '-GUI-CLOSE-':
            break  

    # remove window from the screen
    window.close()  


if __name__ == "__main__":

    # TESTING 
    test_dataframe = pd.read_excel("data.xlsx", sheet_name="shopping")
    test_title = "Shopping"
    test_result = open_dataframe(test_dataframe, test_title)
    print(f"open_choice_test - {test_result} - has been selected")