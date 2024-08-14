from TreeNode import TreeNode
class Tree():
    def __init__(self, rootName: str) -> None:
        self.root = TreeNode(rootName)
        self.nodeCount = 1

    def AddChildren(self, parent: TreeNode, newChild: TreeNode) -> None:
        parent.children.append(newChild)
        self.nodeCount+=1

    def GetChildrenName(self, parent: TreeNode) -> list:
        res = []
        for childNode in parent.children:
            res.append(childNode.nodeName)
        return res

    def GetChildrenNode(self, parent: TreeNode) -> list:
        return parent.children

    def RenameNode():
        pass

    # Searching
    # BFS: use queue, pop at front to check
    def BFS(self, target: str) -> bool:
        trace: list[str] = []
        queue: list[TreeNode] = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0) # difference here
            trace.append(node.nodeName)
            queue += node.children
            if node.nodeName == target:
                print(trace)
                return True
        print(trace)
        return False
    
    # DFS: use stack, pop at the end to check
    def DFS(self, target: str) -> bool:
        trace: list[str] = []
        stack: list[TreeNode] = []
        stack.append(self.root)

        while stack:
            node = stack.pop() # difference here, 
            trace.append(node.nodeName)
            stack += node.children
            if node.nodeName == target:
                print(trace)
                return True
        print(trace)
        return False

    

'''
           A
        /  |  \
       B   C    D
      /  / | \  | \
     E  F  G  H I  J
  '''

tree = Tree("A")

tree.AddChildren(tree.root, TreeNode("B"))
tree.AddChildren(tree.root, TreeNode("C"))
tree.AddChildren(tree.root, TreeNode("D"))

# Add node to node B
tree.AddChildren(tree.root.children[0], TreeNode("E"))

# Add node to node C
tree.AddChildren(tree.root.children[1], TreeNode("F"))
tree.AddChildren(tree.root.children[1], TreeNode("G"))
tree.AddChildren(tree.root.children[1], TreeNode("H"))

# Add node to node D
tree.AddChildren(tree.root.children[2], TreeNode("I"))
tree.AddChildren(tree.root.children[2], TreeNode("J"))
