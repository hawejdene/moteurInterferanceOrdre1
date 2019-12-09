import copy

from model.Fait import Fait
from model.Predicat import Predicat
from model.Regle import Regle
from model.Operation import Operation

# retourn list apres remplacer les subititutions de l'unification
def listSubitute(list, dict):
    i = 0
    while i < len(list):
        for d in dict:
            if list[i] == d:
                print("listSubitute" ,list[i], dict[d])
                list[i] = dict[d]
                break
        i += 1
    return list

# dict unificateur
def opeartionSubtitue(operation: Operation, dict):
    print('dict', dict)
    for d in dict:
        print("d ", d, dict[d])
        if d in operation.att1:
            operation.att1 = operation.att1.replace(d, dict[d])
            print("ATTT1111", operation.att1)
        if d in operation.att2:
            operation.att2 = operation.att2.replace(d, dict[d])
            print("ATTT2", operation.att2)

    if '?x' not in operation.att1 and '?y' not in operation.att1:
        operation.att1 = str(eval(operation.att1))
        print('eval ',operation.att1 )

    if '?x' not in operation.att2 and '?y' not in operation.att2:
        operation.att2 = str(eval(operation.att2))
        print('eval ', operation.att2)
    return operation


def is_atom(expr):
    return len(expr) == 1


def is_variable(expr):
    return '?' in expr


def unifier_atom(expr1, expr2):
    print('unifier atome')

    if is_atom(expr1):
        expr1 = expr1[0]
    if is_atom(expr2):
        expr1, expr2 = expr2[0], expr1
    print(expr1, expr2)
    if expr1 == expr2:
        return {}
    if is_variable(expr2):
        expr1, expr2 = expr2, expr1
    if is_variable(expr1):
        if expr1 in expr2:
            return None
        if is_atom(expr2):
            return {expr1: expr2[0]}
        return {expr1: expr2}
    return None


def unifier(terms1, terms2):
    print('\n')
    print('unifier', terms1, terms2)
    if is_atom(terms1) or is_atom(terms2):
        return unifier_atom(terms1, terms2)
    F1, F2 = [], []
    print(F1)
    F1.append(terms1.pop(0))
    T1 = terms1
    F2.append(terms2.pop(0))
    T2 = terms2
    print('F1=', F1)
    print('T1=', T1)
    print('F2=', F2)
    print('T2=', T2)
    Z1 = unifier(F1, F2)
    if Z1 is None:
        return None

    print('T1=', T1)

    print('T2=', T2)

    T1 = listSubitute(T1, Z1)
    T2 = listSubitute(T2, Z1)
    print('T1=', T1)

    print('T2=', T2)

    Z2 = unifier(T1, T2)
    if Z2 is None:
        return None
    Z2.update(Z1)
    return Z2


def genererConclusionUnifies(reglos, pred: Predicat):
    reglesExecutable = []
    regles = copy.deepcopy(reglos)

    for regle in regles:
        print('====================')
        print('num : ', regle.rang)
        print(pred)
        predicatvals1 = regle.predicats[0].vals.copy()
        predicatvals2 = pred.vals.copy()
        unificateur = unifier(predicatvals1, predicatvals2)

        if unificateur != None:
            i = 0
            test = True
            while i < len(regle.operations) and test:
                operation = opeartionSubtitue(regle.operations[i], unificateur)
                print("OPERATION", i, operation)
                i += 1
                if not operation.verifOperation():
                    test = False
            if test:
                print("REGLE A EXECUTER", regle.rang)
                reglesExecutable.append({regle.rang: unificateur})

    conclusionUnifies = unifierConclusion(reglesExecutable, regles)
    for conclusion in conclusionUnifies:
        print(conclusion)
    print('-----------------')
    return conclusionUnifies


def unifierConclusion(reglesDeclenchables, regles):
    # Contient les conclusion unifiées
    x = '?x'
    y = '?y'
    conclusionsUnifies = []

    for regleDeclenchable in reglesDeclenchables:

        key = list(regleDeclenchable.keys())[0]
        value = list(regleDeclenchable.values())[0]

        for regle in regles:
            if regle.rang == key:
                conclusion = regle.conclusion

                # Extracting variables from unification result
                if '?y' in value.keys():
                    y = value['?y']
                if '?x' in value.keys():
                    x = value['?x']

                # Remplacer les variables de la conclusion selon l'unification
                substitutionX = [variable.replace('?x', x) if '?x' in variable else variable for variable in
                                 conclusion.vals]
                substitutionY = [variable.replace('?y', y) if '?y' in variable else variable for variable in
                                 substitutionX]

                # Calculating with eval
                vals = [eval(operation) for operation in substitutionY]
                # Converting int to string as eval return int
                valsString = [str(string) for string in vals]

                conclusion.vals = valsString

                conclusionsUnifies.append(conclusion)
                break
    return conclusionsUnifies

def exist(conclusion, predicats):
    if not predicats:
        return False
    verif = False
    for predicat in predicats:
        if predicat.vals[0] == conclusion.vals[0] and predicat.vals[1] == conclusion.vals[1]:
            return True

    return verif



def heuristic(predicat):
    if eval(predicat.vals[0]) == 2:
        return 0
    if (eval(predicat.vals[0]) + eval(predicat.vals[1])) < 2:
        return 7
    if eval(predicat.vals[1]) > 2:
        return 3
    return 1


def getNodewithLowestCost(list, cost_so_far):
    minNode = list[0]
    for node in list:
        if (heuristic(node) + getCostFromList(cost_so_far, node)) < (
                heuristic(minNode) + getCostFromList(cost_so_far, minNode)):
            minNode = node
    heuri = heuristic(minNode) + getCostFromList(cost_so_far, minNode)
    return heuri, minNode, list.index(minNode)


def addPredicatToDict(predicat, dictionnaire, new_val):
    for key in dictionnaire:
        if key.vals[0] == predicat.vals[0] and key.vals[1] == predicat.vals[1]:
            dictionnaire[key] = new_val
            return True
    dictionnaire[predicat] = new_val
    return True


def getCostFromList(dictionnaire, predicat):
    for key in dictionnaire:
        if key.vals[0] == predicat.vals[0] and key.vals[1] == predicat.vals[1]:
            return dictionnaire[key]
    return None


def prepareChemin(chemin, V):
    chemin.append(V)
    chemin.pop(0)
    chemin.reverse()
    return chemin
