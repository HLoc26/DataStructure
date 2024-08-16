from SinglyLinkedList import SinglyLinkedList

l = SinglyLinkedList()

l.InsertEnd("A")
l.InsertEnd("B")
l.InsertEnd("C")
l.InsertEnd("E")
l.InsertEnd("F")
l.InsertEnd("G")

l.PrintList()

l.InsertAt(3, "D")

l.PrintList()