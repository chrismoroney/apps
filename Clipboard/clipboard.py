import sys
import pyperclip as pc
import json

SAVED_DATA_LOCATION = "data.json"

def save(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)

def load(path):
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    except:
        return {}

print("***********CLIPBOARD TOOL STARTED**************")
print()
command = input("ENTER COMMAND HERE: ")
while command != "finish":
    data = load(SAVED_DATA_LOCATION)

    if command == "help":
        print("List of all Clipboard commands:")
        print("add - add a custom value to clipboard (accessible with key)")
        print("load - load a value from your data of keys into your paste function (if key is found)")
        print("remove - removes value and key from data")
        print("show_keys - shows list of all keys")
        print("show_vals - shows list of all values")
        print("check - shows all combinations of keys and corresponding values")
        print("finish - terminates usage of clipboard tool")

    # add value into list of data
    elif command == "add":
        k = input("Enter key: ")
        data[k] = pc.paste()
        save(SAVED_DATA_LOCATION, data)

    # load value from list of data
    elif command == "load":
        k = input("Enter key: ")
        if k in data:
            pc.copy(data[k])
        else:
            print("Key not found")

    # remove value in list of data
    elif command == "remove":
        k = input("Enter key: ")
        if k in data:
            del data[k]
        else:
            print("Key not found")
        save(SAVED_DATA_LOCATION, data)

    # prints all possible keys in data
    elif command == "show_keys":
        for k in data.keys():
            print(k)

    # prints all possible values in data
    elif command == "show_vals":
        for k in data:
            print(data[k])

    # check list of all data
    elif command == "check":
        print(data)

    else:
        print("Illegal command")
    
    print()
    command = input("ENTER COMMAND HERE: ")

print("************CLIPBOARD TOOL ENDED***************")