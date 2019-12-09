from model.Fait import Fait
from model.Predicat import Predicat
from model.Regle import Regle


class BaseDeConnaissance:
    def __init__(self, base):
        self.base = base
        self.regles = []
        self.faits = []
        f = open(self.base)
        line = f.readline()
        while line:
            if line != '\n':
                if 'alors' in line:
                    self.regles.append(Regle.extractRegle(line))
                else:
                    self.faits.append(Fait(Predicat.extractPredicat(line)))
            line = f.readline()

    def __str__(self):
        string = 'base\n\tfaits\n'
        for fait in self.faits:
            string += str(fait)
            string += '\n'
        string += '\n'
        for regle in self.regles:
            string += str(regle)
            string += '\n'
        return string
