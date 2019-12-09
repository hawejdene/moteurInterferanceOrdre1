from model import *

class Fait:
    def __init__(self, predicat):
        self.predicat = predicat

    def __str__(self):
        return "\n\t{}".format(self.predicat)