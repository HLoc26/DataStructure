class TreeNode():
    def __init__(self, nodeName: str) -> None:
        self.nodeName: str = nodeName
        self.children: list[TreeNode] = []

    def __repr__(self) -> str:
        return self.nodeName