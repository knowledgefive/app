# knowledgefive version 0.1.0
# an example application in python

# import  modules
import webbrowser
import FreeSimpleGUI as sg                    

# set the GUI theme
sg.theme('Reddit')

def app(startup_message:str):
    '''
    Creat the main application window
    '''

    # check the startup message is a string
    if not isinstance(startup_message, str):
        error_message = f"startup_message {type(startup_message)} is not a str"
        raise ValueError(error_message)
    
    # check the startup message isn't empty
    if len(startup_message) == 0:
        error_message = f"startup_message is empty"
        raise ValueError(error_message)

    # define an application name
    app_name = "KnowledgeFive Application"

    # set menu 
    menu_items = [
        ['&Admin',['&Application Directory']],
         ]
    
    # build GUI components
    top_menu = sg.Menu(menu_items, key='-KF-MENU-')
    instagram_button = sg.Button("Instagram")
    github_button = sg.Button("GitHub")
    message_area = sg.Multiline(startup_message, key='-KF-MESSAGE-', size=(60, 5), disabled=True, no_scrollbar=True)
    status_bar = sg.StatusBar(f'Idle', key='-KF-STATUS-')

    # set the layout of the window contents
    layout = [
        [top_menu],
        [message_area],
        [instagram_button, github_button],
        [status_bar],
               ]

    # create the gui window
    window = sg.Window(app_name, layout, resizable=False, finalize=True, element_justification='c')    

    # loop event to open the window
    while True:
        event, values = window.read()    

        if event == 'Exit' or event ==sg.WIN_CLOSED:
            break  

    # close the main window
    window.close()  

if __name__ == "__main__":

    # define a startup message
    startup_message = "an example application for learning to code"

    # run the application
    app(startup_message)