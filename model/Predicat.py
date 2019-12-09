
class Predicat:
    def __init__(self, nom, vals):
        self.nom = nom
        self.vals = vals

    def __str__(self):
        return '{}({})'.format(self.nom, self.vals)

    @staticmethod
    def extractPredicat(text):
        predicat = Predicat('', [])
        predicat.nom = text.split('(')[0].strip()
        vals = text.split('(')[1].split(')')[0].split(',')
        for val in vals:
            predicat.vals.append(val.strip())
        return predicat

    @staticmethod
    def extractConclusion(conclusion):
        predicat = Predicat('', [])
        predicat.nom = conclusion.split('( ')[0].strip()
        vals = conclusion.split('( ')[1].strip()
        vals = list(vals)
        vals[len(vals) - 1] = ''
        vals = ''.join(vals).strip().split(', ')
        for val in vals:
            print(val)
            predicat.vals.append(val.strip())
        return predicat