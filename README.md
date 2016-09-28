# JS-Browsercheck

## Description
The app checks the js scripts for browser incompatibilties. It uses the website [jscc](http://jscc.info/) to check all js scripts and then stores the "no support" outputs as JSON files (one for each js file). The website and single file checker was created by tbusser. The app uses selenium to access the javascript checker to test which browsers are not compatible with your js scripts and then makes a tabled summary of all your files. The table contains all browsers listed by the website by default and each row represents a function that has no support on at least one browser. The individual cells are coloured red and numbered with the not supported versions. If all versions of the browser support the function then it is coloured green. The results are created in individually numbered folders (format: **yyyymmddhhmmss**), so no data will be overwritten. Data is stored in your home folder under a ./js-browser folder created by the app. Results of individual files are also stored for easier readability of where code modification is needed. Output on terminal at end of running is the location of results folder and its name and list of compaired browser base.

## Installation
### Pre-requirements
- Selenium
- Python3
- Chrome and chromedriver
- Jinja2

### After Pre-requirements are met do the following steps:
1. Go to location you downloaded or cloned the git repo to
2. usage: own_js_tester.py [-fe {JSON,HTML,Markdown,Jira}] location
3. `python3 own_js_tester.py -fe [option] [abs/path/of/folder]`

## Output jira (formated)

![jira_table.png](https://bitbucket.org/repo/AKqgag/images/2486270961-jira_table.png)

## Tests
Manual tests done. Unittests under construction!

## TO-DO
- Error Handling
- Modules
- Jira custom format bug fix
- find embedded js in eg HTML files
- make .sh install script
- Make unit tests

## Release notes
Jira format not copy and paste ready made. Need to remove certain nl and whitespaces.

## Licences
Please check description for Tbusser's [git page](https://github.com/tbusser/jscc) and [website](http://jscc.info/) for the js checker I used.