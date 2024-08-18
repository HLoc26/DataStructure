class BinaryNode():
    def __init__(self, data: int) -> None:
        self.leftNode: BinaryNode = None
        self.rightNode: BinaryNode = None
        self.data: int = data
        self.height: int = 1
        self.children: list[BinaryNode] = []
    
    def __repr__(self) -> str:
        return str(self.data)
        
    def __str__(self) -> str:
        return str(self.data)