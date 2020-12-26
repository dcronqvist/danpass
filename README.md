# danpass
A very simple command line interfaced password manager that uses [fernet encryption](https://asecuritysite.com/encryption/fernet) to store passwords securely.

## Install

Easy installation:

```shell
$ git clone https://github.com/dcronqvist/danpass
$ cd danpass
$ sudo sh ./install.sh  # It'll install it by making a symlink to its location from /usr/local/bin/danpass
```

Or if you prefer a one-line method:

`$ git clone https://github.com/dcronqvist/danpass && cd danpass && sudo sh ./install.sh`

## How to use

Get started by getting familiar with the different commands that exist, you can of course check it all out using `-h`. So by just running `$ danpass -h` will display a bunch of help text.

### Looking up entries
`$ danpass find` will display something like `Found 36 entries in danpass.` depending on how many entries you have stored in danpass. If you also specify `-l` or `--list`, danpass will list all entries in the manager out for you. 

If you instead want to look up a certain entry for a specific site, you can run something like `$ danpass find -l -s example.com` to find the entry associated with the site example.com. Specifying `-l` is necessary since it will make sure danpass actually prints out the entry for you with all the information. If you do not specify `-l`, it will just print out how many entries are associated with the site. `-s` or `--site` followed by the site you wish to search for is how to search for entries given a site.

```
$ danpass find -l -s example.com
Found 1 entries in danpass.
-----------------------------------
ID:             12
Website:        example.com
Username:       johndoe@example.com
Password:       reallygoodpassword
-----------------------------------
```

If you for some reason happen to know the exact `ID` of the entry you'd like to check, then you can simply use the `-id` argument followed by the ID you want to find. Easy peasy.

### Adding entries

When adding an entry to danpass, you have to specify all arguments for it to work. `-s` is the site, `-u` is the username and `-p` is the password that the entry should have.
```
$ danpass add -s example.com -u karendoe@example.com -p karenspassword
Added new entry!
-----------------------------------
ID:             423
Website:        example.com
Username:       karendoe@example.com
Password:       karenspassword
-----------------------------------
```
Badabing badaboom, you got yourself a new entry.

### Updating an entry

If you'd like to change an existing entry, you should first know its ID by using `$ danpass find` beforehand. With the found ID, you can run something like this.
```
$ danpass update -id 423
Found entry:
-----------------------------------
ID:             423
Website:        example.com
Username:       karendoe@example.com
Password:       karenspassword
-----------------------------------
New username: newkarendoe@example.com   <- you will have to input a new username and password here in the terminal.
New password: karensnewpass
-----------------------------------
Updated entry to:
-----------------------------------
ID:             423
Website:        example.com
Username:       newkarendoe@example.com
Password:       karensnewpass
-----------------------------------
```
Super easy to update an entry!

### Deleting an entry

Much like the updating, it's preferred to know the entry's ID for this. Just run the following.
```
$ danpass delete -id 423
Successfully deleted entry:
-----------------------------------
ID:             36
Website:        example.com
Username:       newkarendoe@example.com
Password:       karensnewpass
-----------------------------------
```
And then the entry is deleted, perfect!
