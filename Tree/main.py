from Tree.TreeStructure import Tree
from Tree.TreeNode import TreeNode

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


print(tree.GetAncestors("J"))
