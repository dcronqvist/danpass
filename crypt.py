from cryptography.fernet import Fernet
import config
import os
import sys

def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Create key file
def write_key():
    key = Fernet.generate_key()
    with open(get_script_path() + "/" + config.get_setting("key-file"), "wb") as key_file:
        key_file.write(key)

# Load key file
def load_key():
    if not os.path.isfile(get_script_path() + "/" + config.get_setting("key-file")):
        # First time running danpass!
        # Do some kind of setup maybe?
        write_key()

    return open(get_script_path() + "/" + config.get_setting("key-file"), "rb").read()