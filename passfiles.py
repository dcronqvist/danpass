from cryptography.fernet import Fernet
import crypt
import config
import json

"""
[
    {
        "id": 0,
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
    if encrypted and encrypted != "":
        decrypted = f.decrypt(encrypted)
        # unjson
        entries = json.loads(decrypted)
        return entries
    else:
        return None

def add_entry(site, username, password):
    entries = load_entries()
    new_id = 0

    if entries and len(entries) > 0:
        new_id = entries[-1]["id"] + 1
    else:
        entries = list()

    entry = {
        "id": new_id,
        "site": site,
        "username": username,
        "password": password
    }
    entries.append(entry)
    save_entries(entries)
    return entry

def delete_entry(site, username, password, e_id):
    entries = load_entries()
    if e_id >= 0:
        for entry in entries:
            if entry["id"] == e_id:
                entries.remove(entry)
                save_entries(entries)
                return True, entry

    if entries and site and username and password:
        for entry in entries:
            if entry["site"] == site and entry["username"] == username and entry["password"] == password:
                # found the correct entry!
                entries.remove(entry)
                save_entries(entries)
                return True, entry
    return False, None

def update_entry(site, old_username, old_password, new_username, new_password):
    if delete_entry(site, old_username, old_password, None):
        return add_entry(site, new_username, new_password)
    return None

def get_entries(site):
    entries = load_entries()
    if entries and site:
        found_entries = list()
        for entry in entries:
            if entry["site"] == site:
                found_entries.append(entry)
        return found_entries
    elif entries and not site:
        return entries
    else:
        return []



