class MyString:
    """A class designed operations on a string."""

    name = "My String"

    def __init__(self, string):
        """public constructor"""
        self.string = string
        self.cursor = 0

    def __str__(self):
        """str method"""
        return 'StringOperations(string=' + str(self.string) + ' cursor=' + str(self.cursor) + ')'

    def forward(self, pos):
        """An instance method move cursor forward
           Parameters:
           pos (int): the number of position to move cursor forward
        """
        self.cursor += pos

    def backward(self, pos):
        """An instance method move cursor backward
           Parameters:
           pos (int): the number of position to move cursor backward
        """
        self.cursor -= pos

    def replace(self, character):
        """An instance method move cursor backward
           Parameters:
           character (char): the character to insert at current cursor
        """
        self.string = self.string[:self.cursor] + character + self.string[self.cursor+1:]


class StringController:

    name = 'String Controller'

    def __init__(self, string):
        """public constructor
           Parameters:
           string (str): the string of operations
        """
        import re
        self.operations = list(filter(None, re.split(r'([FBR][\d+\w])', string)))


    def get_operations(self):
        """getter instance method
           Returns (operations) a list of operations"""
        return self.operations


c = StringController('F2B1F5Rw')
s = MyString('abcdefghijklmn')
for o in c.get_operations():
    if o[0] == 'F':
        s.forward(int(o[1]))
    elif o[0] == 'B':
        s.backward(int(o[1]))
    elif o[0] == 'R':
        s.replace(o[1])
    else:
        raise Exception('unrecognized operations', o)

print(s)