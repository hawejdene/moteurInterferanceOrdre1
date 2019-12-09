import collections

from service import algorithmService


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.trace = ''

        self.graph = collections.defaultdict(list)

        def neighbors(self, id):
            return self.graph[id]

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def rechercheProfendeurLimite(self, src, target, maxDepth, chemin):

        if src.vals[0] == target.vals[0] and src.vals[1] == target.vals[1]:
            chemin.append(src)
            return True

        if maxDepth <= 0:
            return False

        for i in self.graph[src]:
            self.trace += str(i) + '\n'
            if self.rechercheProfendeurLimite(i, target, maxDepth - 1, chemin):
                chemin.append(i)
                return True
        return False

    def rechercheProfendeurLimiteIteratif(self, src, target, maxDepth, chemin):
        self.trace += ''
        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            self.trace += '__________depth' + str(i) + '_________\n'
            if self.rechercheProfendeurLimite(src, target, i, chemin):
                return True
        return False

    def a_star_search(self, start, goal):
        self.trace = ''
        openstates = [start]
        cost_so_far = {start: 0}
        came_from = {start: None}
        closed = []
        parcours = []
        while openstates:
            heuri, selected, index = algorithmService.getNodewithLowestCost(openstates, cost_so_far)
            openstates.pop(index)
            closed.append(selected)
            parcours.append(selected)
            self.trace += str(selected) + ' valeur heuristic '+ str(heuri) + '\n'
            if selected.vals[0] == goal.vals[0] and selected.vals[1] == goal.vals[1]:
                parcours.append(selected)
                return True, parcours
            for child in self.graph[selected]:
                if child not in openstates and child not in closed:
                    openstates.append(child)
                    # came_from[child] = selected
                    algorithmService.addPredicatToDict(child, came_from, selected)
                    new_cost = algorithmService.getCostFromList(cost_so_far, selected) + 1 + algorithmService.heuristic(child)
                    algorithmService.addPredicatToDict(child, cost_so_far, new_cost)
                    # cost_so_far[child] = new_cost
                elif child in openstates or child in closed and algorithmService.getCostFromList(cost_so_far,
                                                                                          selected) + 1 < algorithmService.getCostFromList(
                        cost_so_far, child):
                    # cost_so_far[child] = cost_so_far[selected] + 1
                    algorithmService.addPredicatToDict(child, cost_so_far,
                                                algorithmService.getCostFromList(cost_so_far, selected) + 1)
                    openstates.append(child)
                    # came_from[child] = selected
                    algorithmService.addPredicatToDict(child, came_from, selected)

        return False