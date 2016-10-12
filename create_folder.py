#Functions for creating (if needed) new folders for the app
import os
import datetime

def timestamped_foldername():
    '''
        Creates a folder from the current time as a continuous string without ms
        Returns: The name of the folder
    '''
    time = str(datetime.datetime.now())
    time = time.split(".")[0]
    time_date = time.split(" ")[0]
    time_hms = time.split(" ")[1]
    time_date_clumped = time_date.split("-")
    time_date_clumped = ("").join(time_date_clumped)
    time_hms_clumped = time_hms.split(":")
    time_hms_clumped = ("").join(time_hms_clumped)
    folder_name = time_date_clumped+time_hms_clumped+"/"
    return folder_name

def result(location):
    '''
        Checks if main app folder exists and if not make it and after create cw folder
        Args: Where to create result folder
        Resturns: Full path of folder
    '''
    timestamp = timestamped_foldername()
    if not os.path.exists(location):
        os.mkdir(location)
    if not location.endswith('/'):
        location = location+"/"
    cwd = location+timestamp
    if not os.path.exists(cwd):
        make_timestamp_folder = os.mkdir(cwd)
    return cwd
