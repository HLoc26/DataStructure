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
        
    # Deletion
    # Delete head
    def DeleteHead(self) -> Node:
        if self.head == None:
            return None
        head = self.head
        head.data = None
        self.head = head.next
        del head
        self.length -= 1
        return self.head
    
    # Delete end
    def DeleteEnd(self) -> Node:
        if self.head == None:
            return None
        curNode = self.head
        while curNode.next.next != None:
            curNode = curNode.next
        tail = curNode.next
        tail.data = None
        curNode.next = None
        del tail
        self.length -= 1
        return self.head
    
    # Delete at a specific position
    def DeleteAt(self, position: int) -> Node:
        '''0-indexed, meaning head is at position 0'''
        if position >= self.length:
            return self.DeleteEnd()
        if position == 0:
            return self.DeleteHead()
        curPos = 0
        curNode = self.head
        while curPos + 1 != position and curNode.next != None:
            curPos+=1
            curNode = curNode.next
        target = curNode.next
        target.data = None
        curNode.next = curNode.next.next
        del target
        return self.head
    
    # Reverse a singly linked list
    def Reversed(self) -> Node:
        curNode = self.head
        prevNode = None

        while curNode != None:
            nextNode = curNode.next

            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        
        self.head = prevNode
        return self.head
