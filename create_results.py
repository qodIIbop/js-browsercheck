#Functions for creating visual results
import os
import json
import re

import config

def json_file(from_w_files, location, fname):
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
    result.close()
    return 1

def table_view(result_json_loc, location, fname, ext):
    '''
        Exports results to a table style of chose and saves extension ext setting
        Args:
             result_json_loc: where to look for result JSON file
             location: Where to save the result file
             fname: What to save result file as (no extension added)
             ext: the extension of the new file
             browsernamefile: list of browsers checked against
        Returns: HTML if is_HTML is Yes
                 md if is_HTML is No
    '''
    template_data = {}
    with open(config.BROWSERNAME_JSON, "r") as get_bnames:
        template_data["browsername"] = json.load(get_bnames)
    get_bnames.close()
    fname = fname + "." + ext
    result_table = location+"/"+fname
    with open(result_json_loc, "r") as input_file:
        data = json.load(input_file)
        values = list(data.values())
    input_file.close()
    for index, key in enumerate(data):
        browsers = values[index]
        template_data[key] = {}
        for browser in browsers:
            re_result = re.search('\D*', browser)
            browser_name = (str(re_result.group())).strip()
            version = re.search(config.REGEX_VERSION_SEARCH, browser)
            template_data[key][browser_name] = version.group()
        with open(result_table, "w") as result_file:
            if ext in ["md","html"]:
                template = config.ENV.get_template('html_template.html')
            elif ext == "jira":
                template = config.ENV.get_template('jira_custom.txt')
            else:
                return "Error: Unknown template!"
            template_content = template.render(template_data = template_data)
            result_file.write(template_content)
        result_file.close()
    return ext

#old function. Improved above
def HTML(result_json_loc, location, fname, is_HTML):
    '''
        Exports results to a HTML5 tag table and saves extension as .html or .md (markdown) depending on is_HTML input_file
        Args:
             result_json_loc: where to look for result JSON file
             location: Where to save the result file
             fname: What to save result file as (no extension added)
             is_HTML: save as HTMl file or md file
        Returns: HTML if is_HTML is Yes
                 md if is_HTML is Yes
                 0 if neither
    '''
    template_data = {}
    with open(BROWSERNAME_JSON, "r") as get_bnames:
        template_data["browsername"] = json.load(get_bnames)
    get_bnames.close()
    if is_HTML == "Yes":
        fname = fname + ".html"
        HTML = True
    elif is_HTML == "No":
        fname = fname + ".md"
        HTML = False
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

#old function. Improved above
def JIRA(result_json_loc, location, fname):
    '''
        Exports results to a jira custom format
        Args:
             from_w_files: where to look for JSON files to check for duplicates
             location: Where to save the result file
             fname: What to save result file as
    '''
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
