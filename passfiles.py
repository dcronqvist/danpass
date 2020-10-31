from cryptography.fernet import Fernet
import crypt
import config
import json

"""
[
    {
        "site": "example.com",
        "username": "daniel",
        "password": "coolestguyontheblock"
    }
]

List of entries -> json the list -> encrypt the json'd list -> fill file with this encrypted json'd list
File with encrypted json'd list -> (decrypt) json'd list -> un'json'd list of entries

"""

def save_entries(entries):
    # create fernet object
    f = Fernet(crypt.load_key())
    # json the list
    j = json.dumps(entries)
    # encrypt json
    encrypted = f.encrypt(j.encode())
    # save to file
    with open(config.get_setting("passwords-file"), "wb") as file:
        file.write(encrypted)

def load_entries():
    #create fernet object
    f = Fernet(crypt.load_key())
    # read file
    with open(config.get_setting("passwords-file"), "rb") as file:
        encrypted = file.read()
    # decrypt
    decrypted = f.decrypt(encrypted)
    # unjson
    entries = json.loads(decrypted)
    return entries

def add_entry(site, username, password):
    entry = {
        "site": site,
        "username": username,
        "password": password
    }
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)

