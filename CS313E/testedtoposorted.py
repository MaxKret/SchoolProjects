  # return a list of vertices after a topological sort
def toposort (self):
    nVerts = len(self.Vertices)
    
    # Make a copy of the Graph
    copyGraph = Graph()
    for v in self.Vertices:
      copyGraph.addVertex(v.label)
    for i in range(nVerts):
      for j in range(nVerts):
        copyGraph.addDirectedEdge(i, j, self.adjMat[i][j])  
    
    # Return empty list if cycle is present
    sorted = []
    if self.hasCycle():
      return sorted
    
    # Go through adjacency matrix until a vertex with no
    #   successor is found. This vertex is then added to the
    #	list "sorted", and deleted from the adjacency matrix.
    #   These steps are repeated until the adj. matrix is empty.
    while nVerts > 0:    
      row = 0
      while row < nVerts:
        for j in range(nVerts):
          if copyGraph.adjMat[row][j] != 0:
            row += 1
            break
            
        # If the row has all zeros, then it is
        #   added to the end of our topological sort list
        if j == nVerts - 1:
          # lastVert should have no successors
          lastVert = copyGraph.Vertices[row]
          sorted.insert(0, lastVert)
          copyGraph.deleteVertex(lastVert.label)
          break
      nVerts -= 1      
      
    return sorted