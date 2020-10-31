import crypt
import passfiles
import argparse

parser = argparse.ArgumentParser(description="Manage your passwords!")
parser.add_argument("A", metavar='A', help="The action to take, 'find', 'add', 'update' or 'delete'")
parser.add_argument("-s", "--site", metavar="S", help="Specifies site for action")
parser.add_argument("-u", "--username", metavar="U", help="Specifies username for action")
parser.add_argument("-p", "--password", metavar="P", help="Specifies password for action")
parser.add_argument("-l", "--list", action="store_true", help="Specified if you want to print all found entries")
parser.add_argument("-id", type=int, default=None, help="Another way to update or delete entries.")

args = parser.parse_args()

def print_entry(entry, end=False):
    print(f"ID: \t\t{entry['id']}")
    print(f"Website: \t{entry['site']}")
    print(f"Username: \t{entry['username']}")
    print(f"Password: \t{entry['password']}")

# FIND
if args.A.lower() == 'find':
    entries = passfiles.get_entries(args.site)
    print(f"Found {len(entries)} entries in danpass.")
    if args.list and len(entries) > 0:
        print("-----------------------------------")
        for entry in entries:
            print_entry(entry)
            print("-----------------------------------")

# ADD
if args.A.lower() == 'add' and args.site and args.username and args.password:
    entry = passfiles.add_entry(args.site, args.username, args.password)
    print("Added new entry!")
    print("-----------------------------------")
    print_entry(entry)
    print("-----------------------------------")

# DELETE
if args.A.lower() == 'delete' and ((args.site and args.username and args.password) or args.id >= 0):
    succ, ent = passfiles.delete_entry(args.site, args.username, args.password, args.id)
    if succ:
        print("Successfully deleted entry:")
        print("-----------------------------------")
        print_entry(ent)
        print("-----------------------------------")
    else:
        print("Could not find such an entry.")


