from .TreeNode import TreeNode
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
            res.append(childNode.data)
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
            if currNode.data == target:
                currNode.data = newName
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
                if child.data == target:
                    return nodeChildren
                else:
                    deque.extend(child.children)
                childrenCount -= 1
        return None

    # Get ancestors
    def GetAncestors(self, target: str) -> list[TreeNode]:
        ancestors = []
    
        def dfs(node: TreeNode) -> bool:
            for child in node.children:
                if child.data == target:
                    ancestors.append(node)
                    return True
                if dfs(child):
                    ancestors.append(node)
                    return True
            return False

        dfs(self.root)
        return ancestors[::-1]

    # Searching
    # BFS: use queue, pop at front to check
    def BFS(self, target: str) -> list:
        trace: list[TreeNode] = []
        queue: list[TreeNode] = []
        queue.append(self.root)

        while queue:
            node = queue.pop(0) # different to DFS here
            trace.append(node)
            queue += node.children
            if node.data == target:
                return [True, trace]
        return [False, None]
    
    # DFS: use stack, pop at the end to check
    def DFS(self, target: str) -> list:
        trace: list[TreeNode] = []
        stack: list[TreeNode] = []
        stack.append(self.root)

        while stack:
            node = stack.pop() # difference here, 
            trace.append(node)
            stack += node.children
            if node.data == target:
                return [True, trace]
        return [False, None]
