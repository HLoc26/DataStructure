from SinglyLinkedList import SinglyLinkedList

l = SinglyLinkedList()

l.InsertEnd(10)
l.InsertEnd(20)
l.InsertEnd(30)
l.InsertEnd(40)
l.InsertEnd(50)
l.InsertEnd(60)

l.PrintList()
# l.Reversed()
# l.PrintList()

l.Rotate(4)
print(l)