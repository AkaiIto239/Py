'''
Implementiere eine Klasse für gewichtete Graphen sowie eine 
Methode, die den Dijkstra-Algorithmus implementiert.

Rückgabe des Algorithmus soll ein Dictionary sein, dessen Schlüssel die
Knoten des Graphen und dessen Werte Paare aus 1. der Distanz zum
Startknoten und 2. dem Vorgängerknoten bei der Berechnung dieser Distanz
sind.
'''

from collections import defaultdict

class WeightedGraph:
    def __init__(self):
        self.wg = defaultdict(set)
    def add_edge(self, src, tgt, weight):
        #self.wg[src] = []
        self.wg[src].add((tgt,weight))
    def has_edge(self, src, tgt):
        for val in self.wg[src]:
            if val[0] == tgt:
                return True
        return False

    def target_nodes(self, node):
        return self.wg[node]
    # ...
    # ggf weitere Methoden
    # ...
    def dijkstra(self, src):
        # soll 2 Dictionaries liefern: Erstes dict gibt für jeden Knoten
        # seinen Vorgänger an, zweites dict gibt für jeden Knoten die Kosten
        # des kürzesten Pfades an
        
        src_dict = defaultdict(set)
        cost_dict = defaultdict(list)
        cost_dict[src] = 0
        active_node = src
        visited = set()
        other_edges = []
        result_dict = {src:(0, '')}
        while True:
            current_nodes = []
            visited.add(active_node)
            adjacentNodes = WeightedGraph.target_nodes(self, active_node)

            for item in adjacentNodes:
                if not item[0] in visited:
                    current_nodes.append((item[1],item[0]))
            try:
                cheapest_edge = current_nodes.pop(current_nodes.index(min(current_nodes)))
            except ValueError:
                return result_dict

            for item in current_nodes:
                    other_edges.append((item[0],item[1]))

            min_edge = (10000000, '')

            if other_edges != []:
                min_edge = min(other_edges)
                
            if min_edge[0] < cheapest_edge[0]:
                if min_edge[1] not in visited:
                    cost_dict[min_edge[1]] = min_edge[0]
                    src_dict[min_edge[1]] = src_dict[active_node]
                    x = src_dict[min_edge[1]]
                    result_dict[min_edge[1]] = (cost_dict[min_edge[1]] + (result_dict[x][0]), x)
                    active_node = min_edge[1]
                    del other_edges[other_edges.index(min_edge)]
            elif cheapest_edge[0] < min_edge[0]:
                if cheapest_edge[1] not in visited:
                    cost_dict[cheapest_edge[1]] = cheapest_edge[0]
                    src_dict[cheapest_edge[1]] = active_node
                    x = src_dict[cheapest_edge[1]]
                    result_dict[cheapest_edge[1]] = (cost_dict[cheapest_edge[1]] + (result_dict[x][0]), x)
                    active_node = cheapest_edge[1]
            else:
                return result_dict
        

if __name__ == '__main__':
    
    testgraph = WeightedGraph()
    
    testgraph.add_edge('a','b',1)
    testgraph.add_edge('a','d',2)

    testgraph.add_edge('b','c',8)
    testgraph.add_edge('b','e',5)

    testgraph.add_edge('c','f',2)

    testgraph.add_edge('d','e',3)

    testgraph.add_edge('e','c',1)
    testgraph.add_edge('e','f',7)

    testgraph.add_edge('f','e',7)
    
    
    
    print('a: ', testgraph.target_nodes('a'))
    print('b: ', testgraph.target_nodes('b'))
    print('c: ', testgraph.target_nodes('c'))
    print('d: ', testgraph.target_nodes('d'))
    print('e: ', testgraph.target_nodes('e'))
    print('f: ', testgraph.target_nodes('f')) 
    
    print(testgraph.dijkstra('a'))
    print(testgraph.dijkstra('b'))
    print(testgraph.dijkstra('c'))
    print(testgraph.dijkstra('d'))
    print(testgraph.dijkstra('e'))
    print(testgraph.dijkstra('f'))

