class BinaryNode():
    def __init__(self, data: str) -> None:
        self.leftNode = None
        self.rightNode = None
        self.data = data
        self.children: list[BinaryNode] = []

    def __repr__(self) -> str:
        return self.data