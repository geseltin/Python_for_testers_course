import random
from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name # or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
        self.header = header # or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
        self.footer = footer # or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
        self.id = id

    def __repr__(self):
        return f"{self.id}: {self.name}, {self.header}, {self.footer}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
