import argparse
import subprocess
import time
import os
import json
# import pprint
import datetime
import re

# 3rd party imports
# Needed: selenium and jinja2
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from jinja2 import Environment, PackageLoader

# own imports
import config
import filemod
import create_folder
import filehandling
import create_results
import update


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("location", help="Where are the files to check. Absolute path needed")
    parser.add_argument("-fe", "--file_extension", default="JSON", choices=['JSON','html','md','jira'], help="File format of result file")
    args = parser.parse_args()

    results_folder_path = create_folder.result(config.APP_RESULTS_MAIN_FOLDER)

    for js_file in filehandling.check_js_files(args.location):
        non_compatiblities = {}
        file_content = filehandling.copy_text(js_file)
        browser = webdriver.Chrome()
        browser.get(config.URL)
        assert "JS Compatibility Checker" in browser.title
        text_input = browser.find_element_by_id("txaCode")
        text_input.send_keys(file_content)
        check = browser.find_element_by_xpath("//form/button")
        check.click()
        time.sleep(2)
# Check support and save output
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
        filemod.make_output_files(results_folder_path,filemod.filename(js_file, "Yes"),non_compatiblities)
        time.sleep(1)
        browser.quit()
# Analyse all outputs and present in new file
    final_result_folder = os.path.join(results_folder_path, 'Result')
    os.mkdir(final_result_folder)
    create_results.json_file(results_folder_path, final_result_folder, "result.JSON")
    final_result_JSON = os.path.join(final_result_folder, 'result.JSON')
    if args.file_extension != "JSON":
        create_results.table_view(final_result_JSON, final_result_folder, config.RESULT_TABLE_NAME, args.file_extension)
#Print output for user
    print("Check "+results_folder_path+" for results")
    print("Check http://caniuse.com/#comparison for list of checked browsers")

if __name__ == '__main__':
  main()
