import os

def answer(text):
    while (True):
        answer = input(text)
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Unknown sign")

def file_exists(name):
    path = os.getcwd()
    dir = os.path.join(path, name)
    if os.path.exists(dir):
        return True
    else:
        return False

def rename_process(name, new_name):
    if not file_exists(new_name):
        os.rename(name, new_name)
        print("'{0}' is renamed to '{1}'".format(name, new_name))
        return True
    else:
        print("File of this name already exists")
        if answer("Do you want swap this file? [y/n]"):
            temp = "temp"
            os.rename(new_name, temp)
            os.rename(name, new_name)
            os.rename(temp, name)
            return True
    return False

def request_exist(path, answer):
    pathway = os.path.join(path, answer)
    if os.path.exists(pathway):
        return True
    else:
        print("Request doesn't exist  ")
        return False

def show_available(path, opcion):
    for item in os.listdir(path):
        if opcion == "dir" and os.path.isdir(item):
            print(item, end=", ")
        elif opcion == "file" and item is not os.path.isdir(item):
            print(item, end=", ")

def choice_dir(path):
    show_available(path, "dir")
    name = input("\nEnter directory name: ")
    if os.path.isdir(os.path.join(path, name)):
        return name
    else:
        print("Directory doesn't exist  ")
        return False

def choice_file(path):
    show_available(path, "file")
    name = input("\nEnter file name: ") + ".txt"
    if request_exist(path, name):
        return name
    else:
        return False