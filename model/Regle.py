from model.Operation import Operation
from model.Predicat import Predicat


class Regle:
    def __init__(self, rang, conclusion, predicats, operations):
        self.rang = rang
        self.conclusion = conclusion
        self.predicats = predicats
        self.operations = operations

    def __str__(self):
        premisses = ''
        predicats = ''
        for predicat in self.predicats:
            predicats = '\t\t' + predicats + str(predicat) + '\n'
        operations = ''
        for operation in self.operations:
            operations = '\t\t' + operations + str(operation) + '\n'

        return '\nregle' + str(self.rang)  + ': si' + predicats +  str(
            operations) + '\talors ' + '\t\t' + str(
            self.conclusion)

    @staticmethod
    def extractRegle(text):
        regle = Regle(0, '', [], [])
        regle.rang = text.split(':')[0]
        premisses = text.split(':')[1].split(' alors ')[0]
        conclusion = text.split(':')[1].split(' alors ')[1]
        regle.conclusion = Predicat.extractConclusion(conclusion)
        for premisse in premisses.split(' et '):
            if not (
                    '<=' in premisse or '>=' in premisse or '<' in premisse or '>' in premisse or '==' in premisse or '=' in premisse):
                regle.predicats.append(Predicat.extractPredicat(premisse.replace('Si ', '')))
            else:
                regle.operations.append(Operation.extractOperation(premisse))

        return regle
