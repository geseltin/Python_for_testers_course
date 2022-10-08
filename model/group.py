import random


class Group:

    def __init__(self, name=None, header=None, footer=None):
        self.name = name or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
        self.header = header or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
        self.footer = footer or ''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8))
