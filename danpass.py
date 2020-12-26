import passfiles
import argparse

parser = argparse.ArgumentParser(description="Manage your passwords!")
parser.add_argument("A", metavar='A', help="The action to take: 'find', 'add', 'update' or 'delete'")
parser.add_argument("-s", "--site", metavar="S", help="Specifies site for action")
parser.add_argument("-u", "--username", metavar="U", help="Specifies username for action")
parser.add_argument("-p", "--password", metavar="P", help="Specifies password for action")
parser.add_argument("-l", "--list", action="store_true", help="Specified if you want to print all found entries")
parser.add_argument("-id", type=int, default=None, help="Another way to update or delete entries.")
args = parser.parse_args()

# small function for pretty printing an entry
def print_entry(entry, end=False):
    print(f"ID: \t\t{entry['id']}")
    print(f"Website: \t{entry['site']}")
    print(f"Username: \t{entry['username']}")
    print(f"Password: \t{entry['password']}")

# FIND - Search for entries in the .pass file
if args.A.lower() == 'find':
    # get all entries that match with the given site
    # if args.site == None, then entries is a list of
    # all saved entries in the file
    entries = passfiles.get_entries(args.site)
    # print how many entries that were found
    print(f"Found {len(entries)} entries in danpass.")
    # if we specified in the call that we want to list
    # the found entries (-l), then list them
    if args.list and len(entries) > 0:
        print("-----------------------------------")
        for entry in entries:
            print_entry(entry)
            print("-----------------------------------")

# ADD - Create a new entry and save it to the .pass file
if args.A.lower() == 'add' and args.site and args.username and args.password:
    # create the new entry and save it to the file
    entry = passfiles.add_entry(args.site, args.username, args.password, None)
    # pretty print the new entry
    print("Added new entry!")
    print("-----------------------------------")
    print_entry(entry)
    print("-----------------------------------")

# DELETE - Remove an existing entry
if args.A.lower() == 'delete' and ((args.site and args.username and args.password) or args.id >= 0):
    # delete the specified entry, either with the specified id or the specified
    # information of the entry
    succ, ent = passfiles.delete_entry(args.site, args.username, args.password, args.id)
    # if we could successfully delete the entry, tell the user
    if succ:
        print("Successfully deleted entry:")
        print("-----------------------------------")
        print_entry(ent)
        print("-----------------------------------")
    # if not, then tell them that too
    else:
        print("Could not find such an entry.")

# UPDATE - Change an existing entry
if args.A.lower() == "update" and ((args.site and args.username and args.password) or args.id >= 0):
    # if we have specified an id, then find the entry using its id
    if args.id and args.id >= 0:
        entry = passfiles.find_entry_by_id(args.id)
    # if we specified information about the entry, then use that to find it
    elif args.site and args.username and args.password:
        entry = passfiles.find_entry_by_info(args.site, args.username, args.password)
    # pretty print the found entry
    print("Found entry:")
    print("-----------------------------------")
    print_entry(entry)
    print("-----------------------------------")
    # ask for new username and password for the entry
    new_username = input("New username: ")
    new_password = input("New password: ")
    # update the entry
    updated = passfiles.update_entry(entry["site"], entry["username"], entry["password"], new_username, new_password, entry["id"])
    # pretty print the updated entry
    print("-----------------------------------")
    print("Updated entry to: ")
    print("-----------------------------------")
    print_entry(updated)
    print("-----------------------------------")
