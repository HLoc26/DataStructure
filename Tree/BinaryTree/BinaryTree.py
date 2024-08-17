from BinaryNode import BinaryNode
class BinaryTree():
    def __init__(self, rootName: str) -> None:
        self.root = BinaryNode(rootName)
        self.nodeCount = 1
    
    def AddChildren(self, parent, newChild) -> None:
        raise NotImplementedError("BinaryTree class can only use AddLeftChild() or AddRightChild() to insert")

    def AddLeftChild(self, parent: BinaryNode, child: BinaryNode) -> None:
        if parent.leftNode == None:
            parent.leftNode = child
            parent.children.insert(0, child)
            self.nodeCount += 1
        else:
            raise KeyError(f"Error add child {child.data} to the left of {parent.data} (left node already exist)")
    def AddRightChild(self, parent: BinaryNode, child: BinaryNode) -> None:
        if parent.rightNode == None:
            parent.rightNode = child
            parent.children.append(child)
            self.nodeCount += 1
        else:
            raise KeyError(f"Error add child {child.data} to the right of {parent.data} (right node already exist)")

    # Traversal
    # Inorder
    def Traverse_Inorder(self, startNode = None) -> list[str]:
        if startNode == None:
            startNode = self.root
        result = []        
        if startNode.leftNode:
            result.extend(self.Traverse_Inorder(startNode.leftNode))
        result.append(startNode.data)
        if startNode.rightNode:
            result.extend(self.Traverse_Inorder(startNode.rightNode))
        return result
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
    # Postorder
    def Traverse_Postorder(self, startNode = None) -> list[str]:
        if startNode == None:
            startNode = self.root
        result = []        
        if startNode.leftNode:
            result.extend(self.Traverse_Postorder(startNode.leftNode))
        if startNode.rightNode:
            result.extend(self.Traverse_Postorder(startNode.rightNode))
        result.append(startNode.data)
        return result

    def print_2d(self):
        COUNT = [5]  # You can adjust this value to change the spacing

        def print_2d_util(node, space):
            if node is None:
                return

            space += COUNT[0]

            print_2d_util(node.rightNode, space)

            print()
            for i in range(COUNT[0], space):
                print(end=" ")
            print(node.data)

            print_2d_util(node.leftNode, space)

        print_2d_util(self.root, 0)
# Create the binary tree
tree = BinaryTree("1")

# Add left and right children to the root
tree.AddLeftChild(tree.root, BinaryNode("2"))
tree.AddRightChild(tree.root, BinaryNode("3"))

# Add children to node 2
tree.AddLeftChild(tree.root.leftNode, BinaryNode("4"))
tree.AddRightChild(tree.root.leftNode, BinaryNode("5"))

# Add a child to node 3
tree.AddLeftChild(tree.root.rightNode, BinaryNode("6"))

# The tree structure now looks like this:
#       1
#      / \
#     2   3
#    / \  /
#   4   5 6

print(tree.Traverse_Inorder())
print(tree.Traverse_Preorder())
print(tree.Traverse_Postorder())

tree.print_2d()