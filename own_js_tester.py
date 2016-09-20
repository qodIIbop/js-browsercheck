import argparse
import subprocess
import time
import os
import json
# import pprint
import datetime

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys

#config
URL = 'http://jscc.info/'
APP_MAIN_FOLDER = os.path.expanduser('~/js-browser/')

def make_cwf():
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

def create_result_folder(location):
    '''
        Checks if main app folder exists and if not make it and after create cw folder
        Args: Where to create result folder
        Resturns: Full path of folder
    '''
    timestamp = make_cwf()
    if not os.path.exists(location):
        os.mkdir(location)
    if location.endswith('/'):
        location = location
    else:
        location = location+"/"
    cwd = location+timestamp
    if not os.path.exists(cwd):
        make_timestamp_folder = os.mkdir(cwd)
    return cwd

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

def filename(js_file, make_json):
    '''
        Gets the name of the file and removes all 'junk' and makes a JSON file (ie.: path and extension)
        /home/user/test/to/given/path/test.js will become test.JSON
        Args: full path to file with filename and extension
        Returns: The name of the file as a JSON file
    '''
    filename = js_file.split("/")
    filename = filename[-1].split(".")
    filename.pop(-1)
    filename = (".").join(filename)
    if make_json == "Yes":
        filename = filename+".JSON"
    else:
         filename = filename
    return filename

def file_open_and_copy_text_function(js_file):
    '''
        Opens a file given in args and returns the content of whole file
        Args: Absolute location of file with name of file
        Returns: whole content of file
    '''
    cur_file = open(js_file, "r")
    functions = cur_file.read()
    cur_file.close()
    return functions

def make_output_files(location, name, text):
    '''
        Creates files from output of the website
        Args: location: The place to save the output file to
              name: Name of the output file
              text: The content of the output file
        Returns: Done or Errorcode
    '''
    filename = location+name
    with open(filename, "w") as results:
        json.dump(text, results, indent=4, sort_keys=True)
    results.close()
    return 1

def create_results(from_w_files, location, fname):
    '''
        Checks all the results for duplicates and saves in a new file without them
        Args: from_w_files: where to look for JSON files to check for duplicates
              location: Where to save the result file
              fname: What to save result file
    '''
    content_result_file = {}
    for root, dirs, files in os.walk(from_w_files, topdown=True, followlinks=False):
        for name in files:
            if name.endswith('.JSON'):
                filepath = ''.join((root, name))
                with open(filepath, "r") as input_file:
                    data = json.load(input_file)
                for index, key in enumerate(data):
                    value = list(data.values())
                    already_known_functions = content_result_file.keys()
                    if key not in already_known_functions:
                        content_result_file[key] = value[index]
    with open(location+"/"+fname, "w") as result:
        json.dump(content_result_file, result, indent=2, sort_keys=True)
    return 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("location", help="Where are the files to check. Absolute path needed")
    args = parser.parse_args()

    results_folder_path = create_result_folder(APP_MAIN_FOLDER)

    for js_file in check_js_files(args.location):
        non_compatiblities = {}
        file_content = file_open_and_copy_text_function(js_file)
        browser = webdriver.Chrome()
        browser.get(URL)
        assert "JS Compatibility Checker" in browser.title
        text_input = browser.find_element_by_id("txaCode")
        text_input.send_keys(file_content)
        check = browser.find_element_by_xpath("//form/button")
        check.click()
        time.sleep(2)
        #check support and save output
        functions = browser.find_elements_by_xpath("//section[@class='report-section']")
        for function in functions:
            function_name = function.find_element_by_xpath("h3/a")
            checked_function = function_name.text
            function_no_support = function.find_elements_by_xpath("section[@data-support='n']/ol/li")
            browsers = []
            for browser_name in function_no_support:
                if browser_name.text:
                    browsers.append(browser_name.text)
                non_compatiblities[checked_function]=browsers
        # pp = pprint.PrettyPrinter(indent=1)
        # pp.pprint(dict(non_compatiblities))
        make_output_files(results_folder_path,filename(js_file, "Yes"),non_compatiblities)
        time.sleep(1)
        browser.quit()
    #analyse all outputs and present in new file
    final_result_folder = results_folder_path+"/Result"
    os.mkdir(final_result_folder)
    create_results(results_folder_path,final_result_folder, "result.JSON")
    print("Check "+results_folder_path+" for results")

if __name__ == '__main__':
  main()
