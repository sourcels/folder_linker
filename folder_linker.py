import sys
from os import listdir, mkdir
from os.path import isfile, join, isdir, abspath
from shutil import copy2, copytree, rmtree
from typing import Any, Tuple

class FolderLinker:
    '''Class FolderLinker'''
    def __init__(self, source: str = None, replica: str = None) -> bool:
        self.source, self.replica = self.get_folder(source=source, replica=replica) # defining source and replica variables
        result = self.paste_in() # replacing files from source into replica

    def get_folder(self, source: str, replica: str) -> Tuple:
        if len(sys.argv) > 2:
            if isdir(sys.argv[1]) and isdir(sys.argv[2]):
                result = (abspath(sys.argv[1]), abspath(sys.argv[2]))
            else:
                result = (None, None)
        elif type(source).__name__ == "str" and type(replica).__name__ == "str":
            if isdir(source) and isdir(replica):
                result = (abspath(source), abspath(replica))
            else:
                result = (None, None)
        else:
            result = (None, None)
        return result

    def paste_in(self) -> None:
        def insert(file: str) -> Any:
            file_path = join(self.source, file)
            file_destination = join(self.replica, file)
            try:
                copytree(file_path, file_destination)
            except NotADirectoryError:
                if isfile(file_path):
                    copy2(file_path, file_destination)
            print(f"{file_path} ---> {file_destination}")

        if self.source != None or self.replica != None:
            print(f"Copying {self.source} folder files into {self.replica} folder...")
            rmtree(self.replica)
            mkdir(self.replica)
            for file in listdir(self.source):
                insert(file)
            return True
        else:
            print("Didn't copied files... Paths doesn't exists")
            return False

if __name__ == "__main__":
    fl = FolderLinker()
