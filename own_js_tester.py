import argparse
import subprocess
import time
import os
import json
# import pprint
import datetime
<<<<<<< HEAD
import re
from shutil import copyfile

# 3rd party imports
# Needed: selenium and jinja2
=======

>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from jinja2 import Environment, PackageLoader

<<<<<<< HEAD
# own module imports

=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
#config
URL = 'http://jscc.info/'
APP_RESULTS_MAIN_FOLDER = os.path.expanduser('~/js-browser/')
APP_FOLDER = os.getcwd()
<<<<<<< HEAD
APP = os.path.join(APP_FOLDER, 'own_js_tester.py')
TEMPLATES = os.path.join(APP_FOLDER, 'templates')
RESULT_TABLE_NAME = 'Final_eval'
ENV = Environment(loader=PackageLoader('own_js_tester','templates'))
BROWSERNAME_JSON = os.path.join(TEMPLATES, 'Browsername.JSON')

#create_folder.py
=======
TEMPLATES = os.path.join(cwd, 'templates')
ENV = Environment(loader=PackageLoader(APP_FOLDER, TEMPLATES))

>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
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

<<<<<<< HEAD
#create_folder.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
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

<<<<<<< HEAD
#filemod.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
def remove_ext(input_file):
    '''
        Removes the extension of a file. Works similar to os.path.splitext
        Args: the file to remove extension of (Full, relative paths can be given and also works on just filenames)
        Returns: the filename without extension
    '''
    filename = input_file.split("/")
    filename = filename[-1].split(".")
    filename.pop(-1)
    filename = (".").join(filename)
    return filename

<<<<<<< HEAD
#filehandling.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
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

<<<<<<< HEAD
#filemod.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
def filename(js_file, make_json):
    '''
        Gets the name of the file and removes all 'junk' and makes a JSON file (ie.: path and extension)
        /home/user/test/to/given/path/test.js will become test.JSON
        Args: full path to file with filename and extension
        Returns: The name of the file as a JSON file
    '''
    # filename = js_file.split("/")
    # filename = filename[-1].split(".")
    # filename.pop(-1)
    # filename = (".").join(filename)
<<<<<<< HEAD
    filename = remove_ext(js_file)
=======
    remove_ext(js_file)
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
    if make_json == "Yes":
        filename = filename+".JSON"
    else:
         filename = filename
    return filename

<<<<<<< HEAD
#filehandling.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
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

<<<<<<< HEAD
#filemod.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
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

<<<<<<< HEAD
#create_results.py
=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
def create_results_JSON(from_w_files, location, fname):
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
<<<<<<< HEAD
    result.close()
    return 1

#create_results.py
def create_results_HTML(result_json_loc, location, fname, is_HTML):
    '''
        Exports results to a HTML5 tag table and saves extension as .html or .md (markdown) depending on is_HTML input_file
        Args:
             result_json_loc: where to look for result JSON file
=======
    return 1

def create_results_HTML(from_w_files, location, fname, is_HTML):
    '''
        Exports results to a HTML5 tag table and saves extension as .html or .md (markdown) depending on is_HTML input_file
        Args:
             from_w_files: where to look for JSON files to check for duplicates
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
             location: Where to save the result file
             fname: What to save result file as (no extension added)
             is_HTML: save as HTMl file or md file
        Returns: HTML if is_HTML is Yes
                 md if is_HTML is Yes
                 0 if neither
    '''
    template_data = {}
<<<<<<< HEAD
    with open(BROWSERNAME_JSON, "r") as get_bnames:
        template_data["browsername"] = json.load(get_bnames)
    get_bnames.close()
=======
    result_table = location+"/"+fname
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
    if is_HTML == "Yes":
        fname = fname + ".html"
        HTML = True
    elif is_HTML == "No":
        fname = fname + ".md"
        HTML = False
<<<<<<< HEAD
    result_table = location+"/"+fname
    with open(result_json_loc, "r") as input_file:
        data = json.load(input_file)
        values = list(data.values())
    input_file.close()
    for index, key in enumerate(data):
        browsers = values[index]
        template_data[key] = {}
        for browser in browsers:
            browser= str(browser)
            browser_name = re.search('\D*', browser)
            version = re.search('\d+\.*\d*-*\d*\.*\d*[\sto\s]*\d+\.*\d*-*\d*\.*\d*', browser)
            template_data[key][browser_name.group()] = version.group()
    with open(result_table, "w") as result_file:
        template = ENV.get_template('html_template.html')
        template_content = template.render(template_data = template_data)
        result_file.write(template_content)
    result_file.close()
    if HTML:
        return "html"
    else:
        return "md"

#create_results.py
def create_results_JIRA(result_json_loc, location, fname):
=======
    template_file = TEMPLATES+"/"+"html_template.txt"
    with open(result_table) as table_result:
        json.dumps(template_file, table_result)
    template = ENV.get_template(result_table)
    template.render()
    if HTML:
        return html
    else:
        return md


def create_results_JIRA(from_w_files, location, fname):
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
    '''
        Exports results to a jira custom format
        Args:
             from_w_files: where to look for JSON files to check for duplicates
             location: Where to save the result file
             fname: What to save result file as
    '''
<<<<<<< HEAD
    template_data = {}
    with open(BROWSERNAME_JSON, "r") as get_bnames:
        template_data["browsername"] = json.load(get_bnames)
    get_bnames.close()
    fname = fname+".txt"
    result_table = location+"/"+fname
    with open(result_json_loc, "r") as input_file:
        data = json.load(input_file)
        values = list(data.values())
    input_file.close()
    for index, key in enumerate(data):
        browsers = values[index]
        template_data[key] = {}
        for browser in browsers:
            browser= str(browser)
            browser_name = re.search('\D*', browser)
            version = re.search('\d+\.*\d*-*\d*\.*\d*[\sto\s]*\d+\.*\d*-*\d*\.*\d*', browser)
            template_data[key][browser_name.group()] = version.group()
    with open(result_table, "w") as result_file:
        template = ENV.get_template('jira_custom.txt')
        template_content = template.render(template_data = template_data)
        result_file.write(template_content)
    result_file.close()
    return 1

=======
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("location", help="Where are the files to check. Absolute path needed")
    parser.add_argument("-fe", "--file_extension", default="JSON", choices=['JSON','HTML','Markdown','Jira'], help="File format of result file")
    args = parser.parse_args()

    results_folder_path = create_result_folder(APP_RESULTS_MAIN_FOLDER)

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
<<<<<<< HEAD
# Check support and save output
=======
        #check support and save output
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
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
<<<<<<< HEAD
# Analyse all outputs and present in new file
    final_result_folder = os.path.join(results_folder_path, 'Result')
    os.mkdir(final_result_folder)
    create_results_JSON(results_folder_path, final_result_folder, "result.JSON")
    final_result_JSON = os.path.join(final_result_folder, 'result.JSON')
    if args.file_extension == "HTML":
        create_results_HTML(final_result_JSON, final_result_folder, RESULT_TABLE_NAME, "Yes")
    elif args.file_extension == "Markdown":
        create_results_HTML(final_result_JSON, final_result_folder, RESULT_TABLE_NAME, "No")
    else:
        create_results_JIRA(final_result_JSON, final_result_folder, RESULT_TABLE_NAME)
=======
    #analyse all outputs and present in new file
    final_result_folder = results_folder_path+"/Result"
    os.mkdir(final_result_folder)
    if args.file_extension == "JSON":
        create_results_JSON(results_folder_path,final_result_folder, "result.JSON")
    elif args.file_extension == "HTML":
        create_results_HTML(,,,"Yes")
    elif args.file_extension == "Markdown":
        create_results_HTML(,,,"No")
    else:
        create_results_JIRA()
>>>>>>> 9418a514979239c19cce14e776324dd7611c64b9
    print("Check "+results_folder_path+" for results")
    print("Check http://caniuse.com/#comparison for list of checked browsers")

if __name__ == '__main__':
  main()
