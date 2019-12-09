from model.BaseDeConnaissance import BaseDeConnaissance
from model.Graph import Graph
from model.Predicat import Predicat
from service import algorithmService
from service.algorithmService import *

base = BaseDeConnaissance("E:/GL4/AI/TPs/TP2-AI/cruches.txt")

for regle in (genererConclusionUnifies(base.regles, Predicat.extractPredicat('cruchesAetB(4,0)'))):
    pass


EtatInit = base.faits[0].predicat
graphe = Graph(EtatInit)
nouedFermées = []
nouedOuverts = [EtatInit]
i = 0

# Graph construction
while nouedOuverts:

    nouedCourant = nouedOuverts.pop(0)
    nouedFermées.append(nouedCourant)
    base.faits = nouedCourant
    possibleConclusions = genererConclusionUnifies(base.regles, nouedCourant)

    for conclusion in possibleConclusions:
        graphe.addEdge(nouedCourant, conclusion)
        if not exist(conclusion, nouedFermées) and not exist(conclusion, nouedOuverts):
            nouedOuverts.append(conclusion)
    i += 1

for key in graphe.graph:
    print("*********")
    print("Sommet: ", key.nom, '(', key.vals, ')')
    print("Values")
    for val in graphe.graph[key]:
        print("fils: ", val.nom, '(', val.vals, ')')

test = Predicat("cruchesAetB", ['4', '2'])
chemin = []
print("=========rechercheProfendeurLimiteIteratif===========")
print(graphe.rechercheProfendeurLimiteIteratif(graphe.V, test, 10, chemin))
chemin = algorithmService.prepareChemin(chemin, graphe.V) # Function that modifies the path in order to get it in a good format
for chem in chemin:
    print(chem)

print("=======a_star_search============")
result, parcours = graphe.a_star_search(graphe.V, test)
for chem in parcours:
    print(chem)
