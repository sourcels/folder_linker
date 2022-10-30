import sys
import logging
from os import listdir, mkdir
from os.path import isfile, join, isdir, abspath
from shutil import copy2, copytree, rmtree
from typing import Any, Tuple
from time import sleep

class FolderLinker:
    '''Class FolderLinker'''
    def __init__(self, source: str = None, replica: str = None, logfile: str = None, interval: int = None) -> None:
        self.source, self.replica = self.get_folder(source=source, replica=replica) # defining source and replica variables
        self.init_logfile(logfile=logfile)
        self.init_interval(interval=interval)

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

    def init_logfile(logfile: str) -> None:
        if isfile(str(logfile)) and str(logfile)[-3:] == "log":
            logname = logfile
            print(f"Successfully took log file as argument!")
        else:
            try:
                logname = sys.argv[3]
                if isfile(logname) and logname[-3:] == "log":
                    print(f"Successfully took log file as argument!")
                else:
                    raise IndexError
            except IndexError:
                logname = "debug.log"
                print(f"Didn't take log file as argument, creating {logname}")
            except Exception as err:
                print(f"Unrecognized error!\nError: {err}")
                return

        logging.basicConfig(filename=logname, # log file
                    filemode='a', # opens for writing, creating if it doesn't exists
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', # format of logging
                    datefmt='%H:%M:%S', # date format
                    level=logging.DEBUG) # logging level

    def init_interval(self, interval: int) -> None:
        if interval and interval > 0:
            self.interval = interval
            logging.info(f"Successfully took interval as argument")
        else:
            try:
                self.interval = int(sys.argv[4])
                if interval > 0:
                    logging.info(f"Successfully took interval as argument")
                else:
                    raise IndexError
            except IndexError:
                self.interval = "debug.log"
                logging.warning(f"Didn't take interval as argument, interval is {self.interval}")
            except Exception as err:
                print(f"Unrecognized error!\nError: {err}")
                return

    def exec(self) -> None:
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
        while self.source != None or self.replica != None:
            logging.info(f"Copying {self.source} folder files into {self.replica} folder...")
            logging.info(f"Removing old {self.replica} folder...")
            rmtree(self.replica)
            logging.info(f"Creating {self.replica} folder...")
            mkdir(self.replica)
            for file in listdir(self.source):
                insert(file)
            sleep(self.interval * 60)
        else:
            logging.error("Didn't copied files... Paths doesn't exists")

if __name__ == "__main__":
    fl = FolderLinker()
    fl.exec()