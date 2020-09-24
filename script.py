# this is a normal python script. Include any logic here.
# imports
import datetime

# logic
def get_current_timestamp():
    return datetime.datetime.now()

def append_to_file(filepath, content):
    with open("testfile.txt", "a") as fh:
        fh.write(content)

FILEPATH = 'testfile.txt'

timestamp = get_current_timestamp()
append_to_file(FILEPATH, '{} some important message\n'.format(timestamp))