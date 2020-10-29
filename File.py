import os
import Function

def create_file(name):
    if not Function.file_exists(name):
        file = open(name, "w")
        file.close()
    else:
        print("File of this name already exist")
        rename_file(name)

def rename_file(name):
    while(True):
        new_name = input("Enter new name: ") + ".txt"
        if Function.rename_process(name, new_name):
            break

def read_file(name):
    f = open(name, "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)
    f.close()

def edit_file(name):
    os.startfile(name)
    while(True):
        if Function.answer("Do You finsihed your edit? [y/n]"):
            break
        else:
            os.startfile(name)

def delete_file(name):
    if Function.answer("Do You want delete your file? [y/n]"):
        print(name + ' is removed.')
        os.remove(name)


