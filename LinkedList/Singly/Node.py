class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next: Node = None

    def __repr__(self) -> str:
        return self.data