import numpy as np
import pandas as pd
import math

nodes= ["A", "B", "C", "D", "E", "F", "G", "H"]
weight_lower_lim = -100
weight_upper_lim = 100

graph_dict = {}

for node in nodes:
    graph_dict[node]=np.random.randint(weight_lower_lim, weight_upper_lim, len(nodes))

#print("Adjacency List: ", graph_dict)

graph_matrix = pd.DataFrame.from_dict(graph_dict, orient="index", columns=nodes)
graph_matrix[graph_matrix<0]=0
graph_matrix.replace(0, math.inf, inplace=True)
for node in graph_matrix.columns:
    graph_matrix[node][node]=0
print("Adjacency Matrix:\n", graph_matrix)

def shortest_path(matrix, start_node, end_node):
    distance_dict={}
    visit_list = []

    for node in matrix.columns:
        distance_dict[node] = [matrix[node][start_node], start_node]
    visit_list.append(start_node)
    print(distance_dict)
    print(visit_list)

    while not all(i in visit_list for i in nodes):
        unvisited_dict = distance_dict.copy()
        visited_nodes = [unvisited_dict.pop(visited_node) for visited_node in visit_list]
        print("Unvisited: ", unvisited_dict)

        current_node=min(unvisited_dict, key=unvisited_dict.get)
        print("Current Node: ", current_node)
        for node in matrix.columns:
            if matrix[node][current_node]+distance_dict[current_node][0] < distance_dict[node][0]:
                distance_dict[node] = [matrix[node][current_node]+distance_dict[current_node][0], current_node]
                print("NODE:", node, distance_dict)

        visit_list.append(current_node)

    print("Final Distances: ", distance_dict)

    final_path = []
    back_node = end_node
    while start_node not in final_path:
        final_path.append(back_node)
        back_node = distance_dict[back_node][1]
    
    final_path.reverse()
    return distance_dict[end_node][0], final_path

print("Shortest Path: ", shortest_path(graph_matrix, "A", "H"))

