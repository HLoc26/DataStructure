class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None

    def __repr__(self) -> str:
        return self.data
    
    def __str__(self) -> str:
        return str(self.data)