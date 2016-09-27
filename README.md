# JS-Browsercheck

## Description
Checks js scripts for browser incompatibilties. Uses [jscc](http://jscc.info/) to check all js scripts and then stores to analysed data in a text file. The website and single file checker was created by tbusser. The app uses selenium to check which browsers are not compatible with your js scripts and then sums up the outputs (in which file with which function which browsers are not compatible)

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

## Tests
No tests where done atm

## TO-DO
- Error Handling
- Modules

## Release notes
n/a

## Licences
Please check description for the Tbusser's [git page](https://github.com/tbusser/jscc) and website for the js checker I used.
