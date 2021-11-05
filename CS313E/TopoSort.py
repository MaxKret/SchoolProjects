#  File: TopoSort.py

#  Description: Use our already built classes for Graph repr. and build upon them with has_cycle and toposort methods.
#               We first test if the given Graph does not contain a cycle and then do a topological sort on that Graph

#  Student Name: Maxwell Kretschmer

#  Student UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 8/8/21

#  Date Last Modified: 8/15/21

import sys

class Stack (object):
    def __init__ (self):
        self.stack = []


    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)


    # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()


    # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]


    # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)


    # return the number of elements in the stack
    def size (self):
        return (len (self.stack))


class Queue (object):
    def __init__ (self):
        self.queue = []


    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)


    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))


    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)


    # return the size of the queue
    def size (self):
        return (len (self.queue))


class Vertex (object):
    def __init__ (self, label):
        self.label = label
        self.visited = False


    # determine if a vertex was visited
    def was_visited (self):
        return self.visited


    # determine the label of the vertex
    def get_label (self):
        return self.label


    # string representation of the vertex
    def __str__ (self):
        return str (self.label)


class Graph (object):
    def __init__ (self):
        self.Vertices = []
        self.adjMat = []


    def unvisit_all(self):
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False


    # check if a vertex is already in the graph
    def has_vertex (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False


    # given the label get the index of a vertex
    def get_index (self, label):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1


    # add a Vertex with a given label to the graph
    def add_vertex (self, label):
        if (self.has_vertex (label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append (Vertex (label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
            (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
            new_row.append (0)
        self.adjMat.append (new_row)


    # add weighted directed edge to graph
    def add_directed_edge (self, start_idx, finish_idx, weight = 1):
        self.adjMat[start_idx][finish_idx] = weight


    # add weighted undirected edge to graph
    def add_undirected_edge (self, start_idx, finish_idx, weight = 1):
        self.adjMat[start_idx][finish_idx] = weight
        self.adjMat[finish_idx][start_idx] = weight


    # get edge weight between two vertices
    # return -1 if edge does not exist
    def get_edge_weight (self, fromVertexLabel, toVertexLabel):
        weight = self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
        if weight != 0:
            return weight
        else:
            return -1


    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors (self, vertexLabel):
        adj_vertices = []
        vertex = self.get_index(vertexLabel)
        for i in range (len(self.Vertices)):
            if (self.adjMat[vertex][i] > 0):
                adj_vertices.append(self.Vertices[i])
        return adj_vertices


    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1


    # get a copy of the list of Vertex objects
    def get_vertices (self):
        return self.Vertices[:]


    # do a depth first search in a graph
    def dfs (self, v):
        # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        self.unvisit_all()


    # do the breadth first search in a graph
    def bfs (self, v):
        # create the Queue
        theQueue = Queue()

        # mark the vertex v as visited and enqueue it
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theQueue.enqueue(v)

        # visit all the other vertices according to breadth
        while (not theQueue.is_empty()):
            base_vertex = theQueue.dequeue()
            # get an adjacent unvisited vertex
            adj_vertex = self.get_adj_unvisited_vertex(base_vertex)
            while (adj_vertex != -1):
                (self.Vertices[adj_vertex]).visited = True
                print (self.Vertices[adj_vertex])
                theQueue.enqueue(adj_vertex)
                
                adj_vertex = self.get_adj_unvisited_vertex(base_vertex)

        # the queue is empty, let us rest the flags
        self.unvisit_all()


    # delete an edge from the adjacency matrix
    # delete a single edge if the graph is directed
    # delete two edges if the graph is undirected
    def delete_edge (self, fromVertexLabel, toVertexLabel):
        self.adjMat[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)] = 0
        self.adjMat[self.get_index(toVertexLabel)][self.get_index(fromVertexLabel)] = 0


    # delete a vertex from the vertex list and all edges from and
    # to it in the adjacency matrix
    def delete_vertex (self, vertexLabel):
        vertex_index = self.get_index(vertexLabel)
        nVert = len(self.Vertices)
        
        # Delete the column
        for i in range(nVert):
            del self.adjMat[i][vertex_index]
        
        # Delete the row
        self.adjMat.pop(vertex_index)
        
        for vertex in self.Vertices:
            if vertex.label == vertexLabel:
                self.Vertices.remove(vertex)
                break



    def has_cycle_helper(self, previous_vertex, current_vertex):
        if current_vertex.was_visited() == True:
            return True
            
        current_vertex.visited = True
        adjacent_vertices = self.get_neighbors(current_vertex.label)
            
        if previous_vertex in adjacent_vertices:
            adjacent_vertices.remove(previous_vertex)
        if len(adjacent_vertices) == 0:
            return False
            
        for neighbor in adjacent_vertices:
            return self.has_cycle_helper(current_vertex, neighbor)


    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self):
        for vertex in self.Vertices: 
            if self.has_cycle_helper(None, vertex):
                return True
      
            # done, unvisit
            self.unvisit_all()

        return False


    #returns the in_degree of a given vertex
    def in_degree(self, vertex):
        vertex_index = self.get_index(vertex.label)
        in_degree = 0
        for i in range(len(self.adjMat)):
            in_degree += self.adjMat[i][vertex_index]
        return in_degree


    # gets in_degree for all vertices in a graph, populating a list with this info
    def populate_in_degreeMat(self):
        degreeMat = []
        for vertex in self.Vertices:
            degreeMat.append(self.in_degree(vertex))
        return degreeMat


    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        # setup
        vertex_queue = Queue()
        deleted_vertex_list = []
        in_degreeMat = []
        sorted_vertices = []


        # if num vertices/len is 1 or 0, graph is sorted
        if len(self.Vertices) <= 1:
            return self.Vertices


        # Make a copy of the graph
        copied_graph = Graph()
        for i in self.Vertices:
            copied_graph.add_vertex(i.label)
        copied_graph.adjMat = self.adjMat[:] 


        # algorithm
        in_degreeMat = copied_graph.populate_in_degreeMat()
        while len(copied_graph.Vertices) > 0:
            for i in range(len(copied_graph.Vertices)):
                # if in_degree is 0 for a vertex, add it to list
                if in_degreeMat[i] == 0:
                    deleted_vertex_list.append(copied_graph.Vertices[i])

            # delete vertices in list
            for i in deleted_vertex_list:
                copied_graph.delete_vertex(i.label)

            # sort deleted list and enqueue
            deleted_vertex_list = sorted(deleted_vertex_list, key=lambda vertex: vertex.label)
            for i in deleted_vertex_list:
                vertex_queue.enqueue(i)

            # reset in_degreeMat and deleted list
            in_degreeMat = copied_graph.populate_in_degreeMat()
            deleted_vertex_list = []


        # dequeue all vertices and return
        for i in range(vertex_queue.size()):
            sorted_vertices.append(vertex_queue.dequeue())

        return [x.label for x in sorted_vertices]


def main():
    # create a Graph object
    theGraph = Graph()


    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int (line)


    # read the vertices to the list of Vertices
    for i in range (num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        theGraph.add_vertex (city)


    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int (line)


    # read each edge and place it in the adjacency matrix
    for i in range (num_edges):
        line = sys.stdin.readline()
        edge = line.strip()
        edge = edge.split()
        start_str = edge[0]
        finish_str = edge[1]
        start_idx = theGraph.get_index(start_str)
        finish_idx = theGraph.get_index(finish_str)

        theGraph.add_directed_edge (start_idx, finish_idx)

    _graph_has_cycle = theGraph.has_cycle()
    # test if a directed graph has a cycle
    if (_graph_has_cycle):
        print ("The Graph has a cycle.")
    else:
        print ("The Graph does not have a cycle.")


    # test topological sort
    if (not _graph_has_cycle):
        vertex_list = theGraph.toposort()
        print ("\nList of vertices after toposort")
        print (vertex_list)


if __name__ == "__main__":
    main()

