class Graph():
    '''General graph data structure.
    
    Inherited by Directed Graph (DGraph) and Undirected Graph (UGraph)'''
    def __init__(self, vertices) -> None:
        self.adjmtx = [[0] * vertices for _ in range(vertices)]
        self.maxStrLen = 1
        
    def add_edge(self, start: int, end: int, weight: int = 1, directed: bool = True) -> None:
        self.adjmtx[start][end] = weight
        if not directed:
            self.adjmtx[end][start] = weight
        self.maxStrLen = max(self.maxStrLen, len(str(weight)))
    
    def print_matrix(self) -> None:
        for row in self.adjmtx:
            for path in row:
                print(f"{path:>{self.maxStrLen + 2}}", end=' ')
            print()

class DGraph(Graph):
    '''Directed Graph data structure
    
    Inherited by Weighted Directed Graph (WDGraph) and Unweighted Directed Graph (UDGraph)'''
    def __init__(self, vertices) -> None:
        super().__init__(vertices)
        
    def add_edge(self, start: int, end: int, weight: int) -> None:
        super().add_edge(start, end, weight, True)

class WDGraph(DGraph):
    '''Weighted Directed Graph'''
    def __init__(self, vertices) -> None:
        super().__init__(vertices)
    
    def add_edge(self, start: int, end: int, weight: int) -> None:
        return super().add_edge(start, end, weight)
    
class UDGraph(DGraph):
    '''Unweighted Directed Graph'''
    def __init__(self, vertices) -> None:
        super().__init__(vertices)
        
    def add_edge(self, start: int, end: int) -> None:
        return super().add_edge(start, end, 1)
        
class UGraph(Graph):
    '''Undirected Graph data structure.
    
    Inherited by Weighted Undirected Graph (WUGraph) and Unweighted Undirected Graph (UUGraph)'''
    def __init__(self, vertices) -> None:
        super().__init__(vertices)
    
    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        super().add_edge(vertex1, vertex2, weight, False)

class WUGraph(UGraph):
    '''Weighted Undirected Graph'''
    def __init__(self, vertices) -> None:
        super().__init__(vertices)
    
    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        return super().add_edge(vertex1, vertex2, weight)

class UUGraph(UGraph):
    '''Unweighted Undirected Graph'''
    def __init__(self, vertices) -> None:
        super().__init__(vertices)
    
    def add_edge(self, vertex1: int, vertex2: int, weight: int) -> None:
        return super().add_edge(vertex1, vertex2, 1)
