import sys
import os
from os.path import isfile, join

class Folder_linker():
    def __init__(self):
        self.get_folder()
        self.skrskra()
    
    def get_folder(self):
        try:
            self.source = sys.argv[1]
            self.replica = sys.argv[2]
        except IndexError as err:
            print(f"Error: Not enough arguments!\nPythonException: {err}")
        finally:
            sys.exit()

    def skrskra(self):
        onlyfans = [f for f in os.listdir(self.source) if isfile(join(self.source, f))]
        print(onlyfans)

fl = Folder_linker()

