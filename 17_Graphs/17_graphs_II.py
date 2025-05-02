class UndirectedGraph:
    def __init__(self, labels):
        '''
        Initialize an undirected graph using
        the provided vertex labels.
        The number of vertices is derived from the length of the labels list.
        An adjacency matrix is created with all entries set to 0.
        '''
        self.labels = labels # e.g. ["A", "B", "C", "D"]
        self.num_vertices = len(labels)
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        
    def label_to_index(self, label):
        '''
        Convert a vertex label to its correspondind index in the maxtrix.
        '''
        if label not in self.labels:
            raise ValueError(f"Label {label} not found in the graph.")
        return self.labels.index(label)
    
    def add_edge(self, label1, label2, weight=1):
        '''
        Add an edge between the vertices with levels 'label1' and 'label2' using the specified weight.
        Because the graph is undirected, the matrix is updated symmetrically.
        '''
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)
        self.adj_matrix[u][v] = weight
        self.adj_matrix[v][u] = weight
    
    def remove_edge(self, label1, label2):
        '''
        Remove the edge between the vertices with labels 'label1' and 'label2'.
        Both entries in the adjacency matrix are set to 0. Reset
        '''
        u = self.label_to_index(label1)
        v = self.label_to_index(label2)
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0
        
    def print_matrix(self):
        '''
        Print the adjacency matrtix with vertex labels.
        '''
        header = "  " + "  ".join(self.labels)
        print(header)
        # Print each row prefixed with the correspsonding label
        for i, row in enumerate(self.adj_matrix):
            row_str = "  ".join(str(x) for x in row)
            print(f"{self.labels[i]} {row_str}")
            
# Define vertex labels
labels = ["A", "B", "C", "D"]

# Create an undirected graph with these labels
graph = UndirectedGraph(labels)

# Add some edges between the vertices
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")
graph.add_edge("B", "C") 

# Print the title of the matrx
print("Adjacency Matrix of the Undirected Graph")
graph.print_matrix()

print(graph.adj_matrix)