import sys, os, logging

VERSION_NUMBER = "V0.2.0" 

def application_path():
    '''
    set the application path for the active application
    '''

    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = os.getcwd()

    return bundle_dir

bundle_dir = application_path()

LOG_FILE = os.path.join(bundle_dir, 'kfive.log')
CONFIG_FILE = os.path.join(bundle_dir, 'config.ini')

def setup_logger(name, log_file, level=logging.DEBUG):
    '''
    setup a logger for information and errors
    '''

    formatter = logging.Formatter('Time:%(asctime)s - Module:%(name)s - Level:%(levelname)s - Message:%(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

def open_directory(directory_path:str):
    '''
    open directory in explorer

    PARAMETERS 
    ----------
    directory_path : str

    '''

    if not os.path.exists(directory_path):
        error_message = f"{directory_path} not found"
        raise FileNotFoundError(error_message)
    
    # open directory in file explorer
    os.startfile(directory_path)


if __name__ == "__main__":

    # test the application directory
    application_directory = application_path()
    print(f"testing application_directory {application_directory}")
    pass