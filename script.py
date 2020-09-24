# this is a normal python script. Include any logic here.
# -------------- imports ----------------------------------
import datetime
import urllib.request, json

# -------------- constants ----------------------------------
FILEPATH = ''
FILENAME = 'loaded_data'
FILE_ENDING = '.json'

# TODO: replace with your API
MY_API = 'http://maps.googleapis.com/maps/api/geocode/json?address=google'


# -------------- logic ----------------------------------
def get_current_timestamp():
    time_stamp =  str(datetime.datetime.now())
    time_stamp =  time_stamp.replace(' ', '_')
    return time_stamp.replace(':', '_')

def write_to_file(filepath, filename, file_ending, content):
    filename = '{path}{name}_{time}{ending}'.format(path=filepath, name=filename, time=get_current_timestamp(), ending=file_ending)
    with open(filename, "a") as fh:
        fh.write(content)

def load_data_from_remote_server(url):
    # load plain data
    with urllib.request.urlopen(url) as url_handler:
        response = url_handler.read().decode()
        # parse to python objects
        data = json.loads(response)
    return data



data = load_data_from_remote_server(MY_API)
print('  {} data entries loaded.'.format(len(data)))
plain_data = str(data)
write_to_file(FILEPATH, FILENAME, FILE_ENDING, plain_data)