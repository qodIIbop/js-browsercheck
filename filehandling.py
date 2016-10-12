# Functions used for checking if files are present and for checking filepath tree
import os

def check_js_files(filepath):
    '''
        Goes through all files and dirs under given root and saves all javascript files and their path to a list
        Args: the root dir
        Returns: a list of all the found js files with location (format: '/home/user/given/path/foundjsfile.js')
    '''
    js_files = []
    for root, dirs, files in os.walk(filepath, topdown=True, followlinks=False):
        for name in files:
            if name.lower().endswith('.js'):
                if root[-1] != "/":
                    path = '/'.join((root, name))
                else:
                    path = "".join((root, name))
                js_files.append(path)
    return js_files

def copy_text(js_file):
    '''
        Opens a file given in args and returns the content of whole file
        Args: Absolute location of file with name of file
        Returns: whole content of file
    '''
    cur_file = open(js_file, "r")
    functions = cur_file.read()
    cur_file.close()
    return functions
