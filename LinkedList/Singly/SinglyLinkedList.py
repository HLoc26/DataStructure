from typing import Any
from Node import Node
class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    # Traversal (print)
    def PrintList(self) -> None:
        curNode = self.head
        while curNode.next != None:
            print(f"{curNode} ->", end=' ')
            curNode = curNode.next
        print("NULL")
    # Insertion
    # At the beginning
    def InsertHead(self, data: object) -> Node:
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.length = 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
        return self.head
    
    # At the end
    def InsertEnd(self, data: object) -> Node:
        newNode = Node(data)
        if self.length == 0:
            return self.InsertHead(data)
        if self.length == 1:
            self.head.next = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        self.length += 1 
        return newNode
    
    # At a specific position
    def InsertAt(self, position: int, data: object) -> Node:
        '''0-indexed, meaning head is at position 0'''
        if position >= self.length:
            return self.InsertEnd(data)
        newNode = Node(data)
        curPos = 0
        curNode = self.head
        while curPos + 1 != position:
            curNode = curNode.next
            curPos += 1
        newNode.next = curNode.next
        curNode.next = newNode
        return newNode
        


