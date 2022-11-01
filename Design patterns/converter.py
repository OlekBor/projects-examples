from abc import ABC, ABCMeta, abstractmethod
from xml.etree.ElementTree import Element, tostring
from testsmod import TestAdapter
import re

# Behavioural Pattern: Template is used here
# 
class Converter(metaclass=ABCMeta):
    def __init__(self, origin, target) -> None:
        self.origin = origin
        self.target = target
        self.original_data = None
        self.converted_data = None

    def convert(self):
#       Defines standard algorithm        
        self.original_data = self.read()
        self.converted_data = [ TestAdapter(*test).get_data_new() for test in self.original_data ]
        self.write(self.converted_data, self.target)


#   These operations have to be implemented in subclasses
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass    


# Behavioural Pattern: Strategy Pattern is used here
# Reference to a File reading strategy is stored in _reader variable
# Can be changed on demand for different variants of reading operation
# For example if data is stored in different format
class TxtToCsv(Converter):
    
    def __init__(self, origin, target) -> None:
        super().__init__(origin, target)
        self._reader = TestReadFromTxt()

    @property
    def reader(self):
        return self._reader

    @reader.setter
    def reader(self, rstrat):
        self._reader = rstrat

    def read(self):
        return self._reader.read(self.origin)

    def write(self, data, target):
        with open(target, 'w') as f:
            headers = ["date", "time", "speed", "distance", "description"]
            f.write(",".join(headers)+"\n")
            f.writelines([ ",".join(test.values())+"\n" for test in data ])

# Same as before, just for writing to XML format
# See details (line 32)
class TxtToXml(Converter):

    def __init__(self, origin, target) -> None:
        super().__init__(origin, target)
        self._reader = TestReadFromTxt()

    @property
    def reader(self):
        return self._reader

    @reader.setter
    def reader(self, rstrat):
        self._reader = rstrat

    def read(self):
        return self._reader.read(self.origin)

    def write(self, data, target):
        with open(target, "wb") as file:
            for n, test in enumerate(data):            
                file.write(tostring(TxtToXml.dict_to_xml(f"test_{n}", test)))
                file.write(b"\n")
    
    @classmethod
    def dict_to_xml(self, tag, d):
        '''
        Turn a simple dict of key/value pairs into XML
        '''
        elem = Element(tag)
        for key, val in d.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
        return elem



class Reader(ABC):

    @abstractmethod
    def read(self, origin):
        pass

# Concrete strategy implementation
class TestReadFromTxt(Reader):
    def read(self, origin):
        with open(origin, 'r') as file:
            lines = file.readlines()
            data = [ re.findall(r'(\d*/\d*/\d*)\s+(\d*:\d*:\d*\s\w*)\s+(\d*)\s+(\d+,\d+)\s+(.*)', line)[0] for line in lines]
        return data

# Example for another reading implementation.
# In case if data stored in different format
# Than it can be used as strategy for concrete implementation of template 'Converter' class
#
#class ExampleReader(Reader):
#    pass

# For testing purposes, while runung as standalone module
if __name__ == '__main__':
    origin = './data/input.txt'
    target = './data/out.csv'
    TxtToCsv(origin, target).convert()
    TxtToXml(origin, './data/out.xml').convert()
