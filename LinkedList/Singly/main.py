from SinglyLinkedList import SinglyLinkedList
from Node import Node
l = SinglyLinkedList()

n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")
n7 = Node("7")
n8 = Node("8")
n9 = Node("9")
n10 = Node("10")

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n5

l.head = n1

if l.DetectLoop() == None:
    l.PrintList()
else:
    l.RemoveLoop()
    l.PrintList()