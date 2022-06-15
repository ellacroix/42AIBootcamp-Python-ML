

from os import sep
from typing import Any


class CsvReader():

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        print('__init__ called')
        self.filename = filename
        self.sep=sep
        self.header=header
        self.skip_top=skip_top
        self.skip_bottom=skip_bottom

    def __enter__(self):
        print('__enter__ called')
        self.file = open(self.filename, 'r')
        self.file.getdata = self.getdata()
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ called')
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        print('getdata called')        
        self.getdata = [["ABC"], ["DEF"]]
        return self.getdata

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        pass

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        print(file.__dict__)
        data = file.getdata()
#        header = file.getheader()
#    with CsvReader('bad.csv') as file:
#        if file == None:
#            print("File is corrupted")

