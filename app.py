# knowledgefive version 0.1.0
# an example application in python

# import modules
import webbrowser, configparser, traceback
import FreeSimpleGUI as sg                    

#import components (local modules)
from components import common

# set the GUI theme
sg.theme('Reddit')

# setup log file
logger = common.setup_logger(__name__, common.LOG_FILE)

# setup config file
config = configparser.ConfigParser()
config.read(common.CONFIG_FILE)

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
        ['&Help',['&Application Directory','&KFive Links' ,'&About']],
         ]
    
    # build GUI components
    top_menu = sg.Menu(menu_items, key='-KF-MENU-')
    error_button = sg.Button("Make Error", key='-KF-ERROR-')
    message_area = sg.Multiline(startup_message, key='-KF-MESSAGE-', size=(60, 5), disabled=True, no_scrollbar=True)
    status_bar = sg.StatusBar(f'Idle', key='-KF-STATUS-')

    # set the layout of the window contents
    layout = [
        [top_menu],
        [message_area],
        [error_button],
        [status_bar],
               ]

    # create the gui window
    window = sg.Window(app_name, layout, resizable=False, finalize=True, element_justification='c')  

    

    # loop event to open the window
    while True:
        event, values = window.read()    

        try:

            ''' PLAY '''
            if event == '-KF-ERROR-':
                raise ValueError("this is a test error")
            
            ''' HELP MENU '''
            if event == 'Application Directory':

                common.open_directory(common.bundle_dir)

            if event == 'KFive Links':

                webbrowser.open("https://linktr.ee/knowledgefive", new=2)

            if event == 'About':

                sg.popup(f"Version:{common.VERSION_NUMBER}")
        
        except Exception as error:
            logger.error(f"Unable to process event {event} due to error {error}\ntraceback {traceback.format_exc()}")
            sg.popup(f"Unable to process event {event} due to error:\n{error}")

         
        if event == 'Exit' or event ==sg.WIN_CLOSED:
            break  

    # close the main window
    window.close()  

if __name__ == "__main__":

    # test config read
    information = config['example']['information']
    logger.debug(f"reading config file {information}")

    # define a startup message
    startup_message = "an example application for learning to code"

    # run the application
    app(startup_message)

    logger.debug("application has started")
