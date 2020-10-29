import os
import Function

def create_dir(name):
    if not os.path.isdir(name):
        os.mkdir(name)
    else:
        print("Directory of this name already exist")
        rename_dir(name)

def rename_dir(name):
    while(True):
        new_name = input("Enter new name: ")
        if Function.rename_process(name, new_name):
            break

def show_content(path):
     print(os.listdir(path), end="\n")

def delete_dir(path, name):
    if not len(os.listdir(os.path.join(path, name))) == 0:
        print("This directory is not empty!")
    if Function.answer("Do You want delete your directory? [y/n]"):
        print(name + ' is removed.')
        os.rmdir(os.path.join(path, name))

