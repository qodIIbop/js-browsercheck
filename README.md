# JS-Browsercheck

## Description
The app checks the js files for browser incompatibilties. It uses the website [jscc](http://jscc.info/) to check all js files and then stores the "no support" outputs as seperate JSON files (one for each js file for easier readability of where code modification is needed). The website and single file checker were created by tbusser. The app uses selenium to access jscc.info to test browser compatibility. The app then makes a tabled summary of all your files. The table contains all browsers listed by the website [caniuse](http://caniuse.com/) and each row represents a function that has no support on at least one browser. The individual cells are coloured red and numbered with the not supported versions (exept jira custom format). If all versions of the browser support the function, then it is coloured green. The results are created in individually numbered folders (format: **yyyymmddhhmmss**), so no data will be overwritten. Data is stored in your home folder under a ./js-browser folder created by the app by default (can be changed in the config file).  Output on terminal at end of running is the location of results folder and its name and a link to the [caniuse](http://caniuse.com/) website to see all browsers the app checks.

## Installation
### Pre-requirements
- Selenium  
- Python3  
- Chrome and chromedriver
- Jinja2

### After Pre-requirements are met do the following steps:
1. Go to location you downloaded or cloned the git repo to  
`cd /path/to/app/root/folder/`
2. usage: own_js_tester.py [-fe {JSON,HTML,Markdown,Jira}] location  
`python3 own_js_tester.py -fe [option] [abs/path/of/folder/to/js]`

## Output HTML and md sample
*(same jinja template is used for both)*
*(Output is coloured. Not visible in sample)*
<table>
    <tr>
        <th></th>
        <th>Android Browser</th>
        <th>Blackberry Browser</th>
        <th>Chrome</th>
        <th>Chrome for Android</th>
        <th>Edge</th>
        <th>Firefox</th>
        <th>Firefox for Android</th>
        <th>IE</th>
        <th>IE Mobile</th>
        <th>Opera</th>
        <th>Opera Mini</th>
        <th>Opera Mobile</th>
        <th>Safari</th>
        <th>Samsung Internet</th>
        <th>UC Browser for Android</th>
        <th>iOS Safari</th>
    </tr>
    <tr>
        <td>Strict mode</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">4 to 12</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">2 to 3.6</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">5.5 to 9</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">9.5-9.6 to 11.6</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">3.1 to 5</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
    </tr>
    <tr>
        <td>Page Visibility</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">4 to 13</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">2 to 9</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">5.5 to 9</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">9.5-9.6 to 12</td>
        <td bgcolor="red">5.0-8.0</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">3.1 to 6</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">3.2 to 6.0-6.1</td>
    </tr>
    <tr>
        <td>FileReader API</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">4 to 5</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">2 to 3.5</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">5.5 to 9</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">9.5-9.6 to 11</td>
        <td bgcolor="red">5.0-8.0</td>
        <td bgcolor="green"></td>
        <td bgcolor="red">3.1 to 5.1</td>
        <td bgcolor="green"></td>
        <td bgcolor="green"></td>
        <td bgcolor="red">3.2 to 5.0-5.1</td>
    </tr>
<table>

## Tests
Manual tests done. Unittests under construction!

## TO-DO
- Error Handling
- find embedded js in eg HTML files
- make .sh install script
- Increase app speed

## Release notes
* Workaround for quick completion. Final version will do the js compatibility checks offline via the data.JSON file provided by [caniuse](http://caniuse.com/)
* JS frameworks that use other formats cannot be detected and therefor cannot be checked (pre-complier needed)
* Tests only done manually on a Ubuntu machine

## Licences
Please check description for Tbusser's [git page](https://github.com/tbusser/jscc) and [website](http://jscc.info/) for the js checker I used.
