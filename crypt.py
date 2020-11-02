from cryptography.fernet import Fernet
import config
import os

# Create key file
def write_key():
    key = Fernet.generate_key()
    with open(os.getcwd() + "/" + config.get_setting("key-file"), "wb") as key_file:
        key_file.write(key)

# Load key file
def load_key():
    if not os.path.isfile(os.getcwd() + "/" + config.get_setting("key-file")):
        # First time running danpass!
        # Do some kind of setup maybe?
        write_key()

    return open(os.getcwd() + "/" + config.get_setting("key-file"), "rb").read()