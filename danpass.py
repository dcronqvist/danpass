import crypt
import passfiles

def print_entry(entry):
    print(f"Website: {entry['site']}")
    print(f"Username: {entry['username']}")
    print(f"Password: t{entry['password']}")