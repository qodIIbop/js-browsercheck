# Functions for removing, changing and creating files
import json

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

def filename(js_file, make_json):
    '''
        Gets the name of the file and removes all 'junk' and makes a JSON file (ie.: path and extension)
        /home/user/test/to/given/path/test.js will become test.JSON
        Args: full path to file with filename and extension
        Returns: The name of the file as a JSON file
    '''
    filename = remove_ext(js_file)
    if make_json == "Yes":
        filename = filename+".JSON"
    return filename

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

def json_prettify(input_file, output_file):
    '''
        Makes indents on a json file
        json_file: Path/to/file
        Returns the path of pretty file
    '''
    with open(input_file, "r") as messy_file:
        text = json.load(messy_file)
        print("File content read")
        messy_file.close()
    with open(output_file, "w") as pretty_file:
        doc = json.dump(text, pretty_file, indent=4)
        print("File prettifyed")
        pretty_file.close()
    return output_file
