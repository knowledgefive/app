# making a simple choice window
# import FreeSimpleGUI module
import FreeSimpleGUI as sg                    

sg.theme('Reddit')

def open_selection(title:str, options:list):
    '''
    create the main GUI window
    '''

    # check if the title is a string
    if not isinstance(title, str):
        error_message = f"title parameters {title} are not a string"
        raise ValueError(error_message)
    
    # check if the string is empty
    if len(title) == 0:
        error_message = f"title is empty"
        raise ValueError(error_message)

    # check if the options are a list
    if not isinstance(options, list):
        error_message = f"options parameters {options} are not a list"
        raise ValueError(error_message)
    
    # check if the option list is empty
    if len(options) == 0:
        error_message = f"options list is empty"
        raise ValueError(error_message)
    
    # setup return value
    selected_value = None
    
    # build GUI components
    selection_title = sg.Text(title)
    selection_combo = sg.Combo(options, default_value="please select an option", font=('Arial Bold', 12), expand_x=True, enable_events=True, readonly=True, size=(5,1), key='-GUI-OPTIONS-')
    selection_confirm = sg.Button('Confirm', key='-GUI-CONFIRM-')

    # set the layout of the window contents
    layout = [
        [selection_title],
        [selection_combo],
        [selection_confirm],
               ]

    # create the gui window
    window = sg.Window("List Options", layout, resizable=False, finalize=True, element_justification='c', size=(500, 100))    

    while True:
        event, values = window.read()    

        if event == '-GUI-CONFIRM-':

            selected_value = values['-GUI-OPTIONS-']      

            if selected_value == "please select an option":
                sg.popup("Please choose an option")
            else:
                break

        if event == 'Exit' or event ==sg.WIN_CLOSED:
            break  

    # Finish up by removing from the screen
    window.close()  

    return selected_value

if __name__ == "__main__":

    # TESTING 
    test_title = "Shopping"
    test_options = ['bread','cheese', 'apple']
    test_result = open_selection(test_title, test_options)
    print(f"open_choice_test - {test_result} - has been selected")