import os

from jinja2 import Environment, PackageLoader

URL = 'http://jscc.info/'
APP_RESULTS_MAIN_FOLDER = os.path.expanduser('~/js-browser/')
APP_FOLDER = os.getcwd()
APP = os.path.join(APP_FOLDER, 'own_js_tester.py')
JSONS = os.path.join(APP_FOLDER, 'Jsonfiles')
TEMPLATES = os.path.join(APP_FOLDER, 'templates')
RESULT_TABLE_NAME = 'Final_eval'
ENV = Environment(loader=PackageLoader('own_js_tester','templates'))
BROWSERNAME_JSON = os.path.join(JSONS, 'Browsername.JSON')
DATA_FILE =  os.path.join(JSONS, 'data.JSON')
REGEX_VERSION_SEARCH = '\d+\.*\d*-*\d*\.*\d*[\sto\s]*\d+\.*\d*-*\d*\.*\d*'
