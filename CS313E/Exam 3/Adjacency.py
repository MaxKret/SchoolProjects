#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610
        
# Given an edge list of a weighted directed graph where each edge is provided as [src, dest, weight],
# return the corresponding adjancency matrix as a 2D list of INTEGERS where the columns and rows are
# sorted by vertex label. Labels may be provided as strings or integers.
def edge_to_adjacency(edge_list):
    # SETUP
    num_edges = len(edge_list)
    vertices_set = set()
    vertices = []

    # GET VERTICES FROM EDGE_LIST
    for edge in edge_list:
        for i in range(len(edge) - 1):
            vertices_set.add(edge[i])
    for vertex in vertices_set:
        vertices.append(vertex)
    vertices = sorted(vertices)
    
    num_vertices = len(vertices)

    the_graph = Graph()

    # ADD VERTICES
    for vertex in vertices:
        the_graph.add_vertex(vertex)

    # ADD EDGES
    for i in range(num_edges):
        the_graph.add_directed_edge(the_graph.get_index(edge_list[i][0]), the_graph.get_index(edge_list[i][1]), edge_list[i][2])


    return the_graph.adjMat


class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []


    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i])):
                return i
        return -1


    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        # add vertex to the list of vertices
        self.Vertices.append(label)

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)


    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight
    

# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()
