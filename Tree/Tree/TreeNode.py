class TreeNode():
    def __init__(self, data: str) -> None:
        self.data: str = data
        self.children: list[TreeNode] = []

    def __repr__(self) -> str:
        return self.data