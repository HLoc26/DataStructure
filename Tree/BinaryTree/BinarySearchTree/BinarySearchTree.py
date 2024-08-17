from BinaryNode import BinaryNode
COUNT = [10]

class BST():
    def __init__(self) -> None:
        self.root: BinaryNode = None
    # Insert
    def Insert(self, value: int) -> BinaryNode:
        if self.root == None:
            self.root = BinaryNode(value)
            return self.root
        curNode = self.root
        while True:
            if value < curNode.data:
                if curNode.leftNode is None:
                    newNode = BinaryNode(value)
                    curNode.leftNode = newNode
                    curNode.children.insert(0, newNode)
                    return self.root
                curNode = curNode.leftNode
            elif value > curNode.data:
                if curNode.rightNode is None:
                    newNode = BinaryNode(value)
                    curNode.rightNode = newNode
                    curNode.children.append(newNode)
                    return self.root
                curNode = curNode.rightNode
            else:
                return self.root
    
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