from cryptography.fernet import Fernet
import config
import os.path

# Create key file
def write_key():
    key = Fernet.generate_key()
    with open(config.get_setting("key-file"), "wb") as key_file:
        key_file.write(key)

# Load key file
def load_key():
    if not os.path.isfile(config.get_setting("key-file")):
        # First time running danpass!
        # Do some kind of setup maybe?
        write_key()

    return open(config.get_setting("key-file"), "rb").read()

# Attempt to load crypto-key
# Will create one if first run.
load_key()