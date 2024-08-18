from BinaryNode import BinaryNode
class AVL():
    def __init__(self) -> None:
        self.root: BinaryNode = None
    
    def GetHeight(self, node):
        '''Returns the height of node. In case node is None, return 0'''
        if not node:
            return 0
        else:
            return node.height
    
    # Insert
    def Insert(self, value: int, node) -> BinaryNode:
        ''' 
            Recursive insertion to add a node to the rooted with node **node**
        '''
        if node == None:
            return BinaryNode(value)
        if type(node) != BinaryNode:
            raise "TypeError: root is not a BinaryNode"
        if value < node.data:
            node.leftNode = self.Insert(value, node.leftNode)
        elif value > node.data:
            node.rightNode = self.Insert(value, node.rightNode)
        else:
            return node # If value == node.data, means the value is in the tree

        # Update the ancestor's height
        node.height = 1 + max(self.GetHeight(node.leftNode), self.GetHeight(node.rightNode))

        # Get the ancestor's balance
        balance = self.GetHeight(node.leftNode) - self.GetHeight(node.rightNode)

        # Left - Left
        if balance > 1 and value < node.leftNode.data:
            return self.RightRotate(node)
        # Right - Right
        if balance < -1 and value > node.rightNode.data:
            return self.LeftRotate(node)
        
        # Left - Right
        if balance > 1 and value > node.leftNode.data:
            node.leftNode = self.LeftRotate(node.leftNode)
            return self.RightRotate(node)
        # Right - Left
        if balance < -1 and value < node.rightNode.data:
            node.rightNode = self.RightRotate(node.rightNode)
            return self.LeftRotate(node)
        return node # Return the new root
    
    # Rotating
    # LeftRotate(a) -> 
    def LeftRotate(self, x: BinaryNode):
        '''Right child (called Y) of node X become node X's parent.
        Node X become the left child of node Y. Returns new root of subtree (in this case, Y).'''
        y = x.rightNode
        T2 = y.leftNode

        # Rotating
        y.leftNode = x
        x.rightNode = T2

        # Update heights
        x.height = 1 + max(self.GetHeight(x.leftNode), self.GetHeight(x.rightNode))
        y.height = 1 + max(self.GetHeight(y.leftNode), self.GetHeight(y.rightNode))

        return y

    # RightRotate(a) -> left child (called b) of node a become node a's parent, node a be ome the right child of node b
    def RightRotate(self, y: BinaryNode):
        '''Left child (called Y) of node X become node X's parent.
        Node X become the right child of node Y. Returns new root of subtree (in this case, Y).
        '''
        # Getting nessesary nodes
        x = y.leftNode
        T2 = x.rightNode

        # Rotating
        x.rightNode = y
        y.leftNode = T2

        # Update heights
        y.height = 1 + max(self.GetHeight(y.leftNode), self.GetHeight(y.rightNode))
        x.height = 1 + max(self.GetHeight(x.leftNode), self.GetHeight(x.rightNode))

        return x

    # Preorder
    def Traverse_Preorder(self, startNode = None) -> list[str]:
        if startNode == None:
            startNode = self.root
        result = []        
        result.append(startNode.data)
        if startNode.leftNode:
            result.extend(self.Traverse_Preorder(startNode.leftNode))
        if startNode.rightNode:
            result.extend(self.Traverse_Preorder(startNode.rightNode))
        return result
    def PrintTree(self):
        def height(node):
            if node is None:
                return 0
            return max(height(node.leftNode), height(node.rightNode)) + 1

        def get_col(h):
            if h == 1:
                return 1
            return get_col(h-1) + get_col(h-1) + 1

        def print_tree_util(M, node, col, row, height):
            if node is None:
                return
            M[row][col] = node.data
            print_tree_util(M, node.leftNode, col-pow(2, height-2), row+1, height-1)
            print_tree_util(M, node.rightNode, col+pow(2, height-2), row+1, height-1)

        h = height(self.root)
        col = get_col(h)
        M = [[0 for _ in range(col)] for __ in range(h)]
        print_tree_util(M, self.root, col//2, 0, h)
        for i in M:
            for j in i:
                if j == 0:
                    print("  ", end="")
                else:
                    print(f"{j:2}", end="")
            print()