import crypt
import passfiles
import argparse

parser = argparse.ArgumentParser(description="Manage your passwords!")
parser.add_argument("--action", metavar='A', help="The action to take, 'find'...")
parser.add_argument("--site", metavar="S", help="Which site to search for.")

args = parser.parse_args()

def print_entry(entry):
    print(f"Website: {entry['site']}")
    print(f"Username: {entry['username']}")
    print(f"Password: {entry['password']}")

if args.action and args.site:
    entry = passfiles.get_entry(args.site)
    print_entry(entry[0])