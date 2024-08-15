from TreeNode import TreeNode
class BinaryNode(TreeNode):
    def __init__(self, nodeName: str) -> None:
        self.leftNode = None
        self.rightNode = None
        super().__init__(nodeName)


    def __repr__(self) -> str:
        return super().__repr__()