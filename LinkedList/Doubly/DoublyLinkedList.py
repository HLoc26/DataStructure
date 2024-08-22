from Node import Node

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def InsertHead(self, data: str) -> Node:
        d = Node(data)
        if self.head == None:
            self.head = d
            self.tail = d
        else:
            self.head.prev = d
            d.next = self.head
            self.head = d
        return self.head
    def InsertTail(self, data:str) -> Node:
        d = Node(data)
        if self.head == None:
            self.head = d
            self.tail = d
        else:
            self.tail.next = d
            self.tail = d
        return self.head
    def PrintList(self) -> None:
        curr: Node = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
        print()

