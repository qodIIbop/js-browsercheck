import argparse
import subprocess
import time
import os

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys

#config
URL = 'http://jscc.info/'
RESULTS = '/home/barnav/temp/'

def check_js_files(filepath):
    '''
        Goes through all files and dirs under given root and saves all javascript files and their path to a list variable
        Args: the root dir
        Returns: a list of all the found js files with location (format: '/home/user/given/path/foundjsfile.js')
    '''
    js_files_path = []
    for root, dirs, files in os.walk(filepath, topdown=True, followlinks=False):
        for name in files:
            if name.lower().endswith('.js'):
                if root[-1] != "/":
                    path = '/'.join((root, name))
                else:
                    path = "".join((root, name))
                js_files_path.append(path)
    return js_files_path

def filename(js_file):
    filename = js_file.split("/")
    return filename[-1]

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

def make_analyse_file(location, name, text):
    '''
        Creates files from output of the website
        Args: location: The place to save the output file to
              name: Name of the output file
              text: The content of the output file
        Returns: Done or Errorcode
    '''
    filename = location+name
    results = open(filename, "a")
    results.write(text)
    results.close()
    return 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("location", help="Where are the files to check. Absolute path needed")
    args = parser.parse_args()

    for js_file in check_js_files(args.location):
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
            checked_function = "\n"+function_name.text+"\n\n"
            make_analyse_file(RESULTS,"asd.txt",checked_function)
            print(checked_function)
            function_no_support = function.find_elements_by_xpath("section[@data-support='n']/ol/li")
            for browser_name in function_no_support:
                not_supported_browser = browser_name.text+"\n"
                print(not_supported_browser)
                make_analyse_file(RESULTS,"asd.txt",not_supported_browser)
        time.sleep(5)
        browser.quit()
    #analyse all outputs and present in new file
    #Delete temp files

if __name__ == '__main__':
  main()
