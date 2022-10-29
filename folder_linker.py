import sys
import logging
from os import listdir, mkdir
from os.path import isfile, join, isdir, abspath
from shutil import copy2, copytree, rmtree
from typing import Any, Tuple

class FolderLinker:
    '''Class FolderLinker'''
    def __init__(self, source: str = None, replica: str = None) -> None:
        self.source, self.replica = self.get_folder(source=source, replica=replica) # defining source and replica variables
        self.logger()
        self.paste_in() # replacing files from source into replica

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

    def logger(self) -> None:
        if len(sys.argv) > 3:
            logname = sys.argv[3]
            if not isfile(logname) and logname[-3:] == "log":
                logname = sys.argv[3]
            else:
                logname = "debug.log"
        else:
            logname = "debug.log"
        logging.basicConfig(filename=logname,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

    def paste_in(self) -> None:
        def insert(file: str) -> Any:
            file_path = join(self.source, file)
            file_destination = join(self.replica, file)
            try:
                copytree(file_path, file_destination)
                logging.info(f"Copy directory {file_path} ---> {file_destination}")
            except NotADirectoryError:
                if isfile(file_path):
                    copy2(file_path, file_destination)
                    logging.info(f"Copy file with metadata {file_path} ---> {file_destination}")

        if self.source != None or self.replica != None:
            logging.info(f"Copying {self.source} folder files into {self.replica} folder...")
            logging.info(f"Removing old {self.replica} folder...")
            rmtree(self.replica)
            logging.info(f"Creating {self.replica} folder...")
            mkdir(self.replica)
            for file in listdir(self.source):
                insert(file)
        else:
            logging.error("Didn't copied files... Paths doesn't exists")
            raise FileNotFoundError("Didn't copied files... Paths doesn't exists")

if __name__ == "__main__":
    fl = FolderLinker()
