

class Operation:
    def __init__(self, att1, att2, op):
        self.att1 = att1
        self.att2 = att2
        self.op = op

    def __str__(self):
        return ' {} {} {}'.format(self.att1, self.op, self.att2)

    def verifOperation(self):
        if self.op == '>=':
            return self.att1 >= self.att2
        if self.op == '<=':
            return self.att1 <= self.att2
        if self.op == '==':
            return self.att1 == self.att2
        if self.op == '=':
            return self.att1 == self.att2
        if self.op == '>':
            return self.att1 > self.att2
        if self.op == '<':
            return self.att1 < self.att2

    @staticmethod
    def extractOperation(text):
        operation = Operation(0, 0, '')
        elems = text.strip()
        elems = elems.split(' ')
        operation.att1 = elems[0].strip()
        operation.att2 = elems[2].strip()
        operation.op = elems[1].strip()
        return operation
