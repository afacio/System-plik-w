import os
import File
import Directory
import Tree
import Function

class Interface():
    def __init__(self):
        self._MENU = "\nAvailable commands:" \
                     "\n- ls\n- tree\n- pwd\n- cd up\n- cd down" \
                     "\n- make dir\n- ren dir\n- del dir" \
                     "\n- make file\n- read file\n- edit file" \
                     "\n- ren file\n- del file\n- exit\n"
        self.program_path = os.getcwd()
        self.home_path = os.path.join(self.program_path, "root")
        self.current_path = self.home_path

        if not os.path.isdir(self.home_path):
            print("root doesn't exist")
            Directory.create_dir("root")
        else:
            print("root is exists")
            if len(os.listdir('./root')):
                print("root isn't empty")
            else:
                print("root is empty")

        os.chdir(self.home_path)

    def choice(self):
        program = True
        while(program):
            choice = input(self._MENU)

            if choice == 'ls':
                Directory.show_content(self.current_path)

            elif choice == 'tree':
                paths = Tree.DisplayablePath.make_tree(self.home_path)
                for path in paths:
                    print(path.displayable())

            elif choice == 'pwd':
                print(self.current_path)

            elif choice == 'cd up':
                Function.show_available(self.current_path, "dir")
                answer = input("Which directory do you want to access?\n")
                if os.path.isdir(os.path.join(self.current_path, answer)):
                    self.current_path = os.path.join(self.current_path, answer)
                    os.chdir(self.current_path)
                    print("Success")
                else:
                    print("Failure")
                print(os.getcwd())

            elif choice == 'cd down':
                if not self.current_path == self.home_path:
                    self.current_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)
                    os.chdir(self.current_path)
                    print("Success")
                else:
                    print("This folder is the lowest ")
                print(os.getcwd())

            elif choice == 'make dir':
                Directory.create_dir(input("Enter directory name:"))

            elif choice == 'ren dir':
                name = Function.choice_dir(self.current_path)
                if name:
                    Directory.rename_dir(name)

            elif choice == 'del dir':
                name = Function.choice_dir(self.current_path)
                if name:
                    Directory.delete_dir(self.current_path, name)

            elif choice == 'make file':
                File.create_file(input("Enter file name:"))

            elif choice == 'read file':
                name = Function.choice_file(self.current_path)
                if name:
                    File.read_file(name)

            elif choice == 'edit file':
                name = Function.choice_file(self.current_path)
                if name:
                    File.edit_file(name)

            elif choice == 'ren file':
                name = Function.choice_file(self.current_path)
                if name:
                    File.rename_file(name)

            elif choice == 'del file':
                name = Function.choice_file(self.current_path)
                if name:
                    File.delete_file(name)

            #elif choice == 'del all':
                #os.chdir(self.program_path)
                #Directory.delete_dir(self.program_path, "root")
                #program = False

            elif choice == 'exit':
                program = False

            else:
                print("Unknown command: " + choice)



