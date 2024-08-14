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

    def RenameNode(self, target: str, newName: str) -> bool:
        '''Return True if successfully renamed, otherwise False'''
        # Use DFS to find
        stack: list[TreeNode] = []
        stack.append(self.root)
        while stack:
            currNode = stack.pop()
            stack.extend(currNode.children)
            if currNode.nodeName == target:
                currNode.nodeName = newName
                return True
        return False
        
    
    # Getting nodes
    # Get root
    def GetRoot(self) -> TreeNode:
        return self.root
    # Get sibblings
    def GetSibblings(self, target: str) -> list[TreeNode]:
        deque: list[TreeNode] = []
        deque.append(self.root)
        while deque:
            parent = deque.pop(0)
            nodeChildren = parent.children
            childrenCount = len(nodeChildren)
            deque.extend(nodeChildren)
            while childrenCount > 0:
                child = deque.pop()
                if child.nodeName == target:
                    return nodeChildren
                else:
                    deque.extend(child.children)
                childrenCount -= 1
        return None

    # Get ancestors

    # Searching
    # BFS: use queue, pop at front to check
    def BFS(self, target: str) -> bool:
        trace: list[str] = []
        queue: list[TreeNode] = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0) # different to DFS here
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
