from SinglyLinkedList import SinglyLinkedList

l = SinglyLinkedList()

l.InsertEnd(10)
l.InsertEnd(20)
l.InsertEnd(30)
l.InsertEnd(30)
l.InsertEnd(20)
l.InsertEnd(10)

l.PrintList()
# l.Reversed()
# l.PrintList()

print(l.IsPalindrome())