from cryptography.fernet import Fernet
import crypt
import config
import json
import os

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
    with open(os.getcwd() + "/" + config.get_setting("passwords-file"), "wb") as file:
        file.write(encrypted)

def load_entries():
    #create fernet object
    f = Fernet(crypt.load_key())
    # read file
    with open(os.getcwd() + "/" + config.get_setting("passwords-file"), "rb") as file:
        encrypted = file.read()
    # decrypt
    if encrypted and encrypted != "":
        decrypted = f.decrypt(encrypted)
        # unjson
        entries = json.loads(decrypted)
        return entries
    else:
        return None

def add_entry(site, username, password, forced_id):
    # load all entries from file
    entries = load_entries()
    # default the new id for the entry to be 0
    new_id = 0

    # if this is not the first run, then use the latest
    # entry's id + 1
    if entries and len(entries) > 0:
        new_id = entries[-1]["id"] + 1
    # if it is the first run, make sure to initialize the entries list
    else:
        entries = list()

    # if we have specified a forced id in the parameters, set the id to this id
    if forced_id >= 0:
        new_id = forced_id

    # create entry object
    entry = {
        "id": new_id,
        "site": site,
        "username": username,
        "password": password
    }
    # add the new entry to the list of entries
    entries.append(entry)
    # finally, save the new list of entries to the file of passwords-file
    save_entries(entries)
    return entry

def delete_entry(site, username, password, e_id):
    # load all entries from .pass file
    entries = load_entries()
    # if we have specified an id to be the entry we want to delete
    if e_id >= 0:
        # look through all entries
        for entry in entries:
            # find the one we're looking for
            if entry["id"] == e_id:
                # remove it and save the new list of entries
                entries.remove(entry)
                save_entries(entries)
                return True, entry

    # if we are not using the id of an entry to find it
    if entries and site and username and password:
        # loop through all entries
        for entry in entries:
            # find the one we're searching for
            if entry["site"] == site and entry["username"] == username and entry["password"] == password:
                # remove the entry and save the list of entries to file
                entries.remove(entry)
                save_entries(entries)
                return True, entry
    # if we haven't found the one that was searched for, return None
    return False, None

def update_entry(site, old_username, old_password, new_username, new_password, e_id):
    # if we successfully found and deleted the specified entry
    if delete_entry(site, old_username, old_password, e_id):
        # then add a new entry with the new details and same id
        return add_entry(site, new_username, new_password, e_id)
    # if we couldn't delete the spec. entry, either it doesn't exist or something else happened
    # then return None.
    return None

def get_entries(site):
    # load all entries in .pass file
    entries = load_entries()
    # if there are entries in the file and we specified a site to search for
    if entries and site:
        # create dummy list of found entries
        found_entries = list()
        # loop through list of entries
        for entry in entries:
            # find entries that have a matching site
            if entry["site"] == site:
                # add these entries to the dummy list of entries
                found_entries.append(entry)
        # return this dummy list of found entries.
        return found_entries
    # if there are entries but we didn't specify a site, then return all entries
    elif entries and not site:
        return entries
    # if there are no entries in the file and we didn't specify a file, then return an empty list
    else:
        return []

def find_entry_by_id(e_id):
    # load all entries from file
    entries = load_entries()
    # loop through all entries
    for entry in entries:
        # check entry matches id
        if entry["id"] == e_id:
            # return that entry
            return entry
    # nothing found, return None
    return None

def find_entry_by_info(site, username, password):
    # load all entries from file
    entries = load_entries()
    # loop through
    for entry in entries:
        # check if entry matches all data
        if entry["site"] == site and entry["username"] == username and entry["password"] == password:
            # return matched entry
            return entry
    # nothing found, return None
    return None



