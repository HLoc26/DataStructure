from Node import Node
class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __repr__(self) -> str:
        res = ""
        curNode = self.head
        while curNode != None:
            res+= f"{curNode} -> "
            curNode = curNode.next
        res += "NULL"
        return res
    # Traversal (print)
    def PrintList(self) -> None:
        curNode = self.head
        while curNode != None:
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
        self.length -= 1
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

    def Rotate(self, k: int) -> Node:
        '''Keep the kth first nodes, move the other nodes to front'''
        if k >= self.length:
            return Node
        
        curNode = self.head
        newLastNode = None
        curPos = 0
        while curNode.next != None:
            if curPos+1 == k:
                newLastNode = curNode
            curNode = curNode.next
            curPos += 1
        newHead = newLastNode.next
        curNode.next = self.head
        newLastNode.next = None
        self.head = newHead
        return self.head

    def IsPalindrome(self) -> bool:
        stack: list[Node] = []
        curNode = self.head
        
        while curNode != None:
            stack.append(curNode)
            curNode = curNode.next

        curNode = self.head
        i = self.length - 1
        while i > self.length // 2:
            last = stack.pop(i)
            if curNode.data != last.data:
                print(curNode.data, last.data)
                return False
            i-=1
            curNode = curNode.next
        return True
    
    def DetectLoop(self) -> Node:
        '''Returns None if there is no loop, otherwise returns the start of the loop'''
        # Use Floyd's algorithm
        slow = fast = self.head

        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # There is no loop, return None
        if slow != fast:
            return None
        # Find the start of loop
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
    
    def RemoveLoop(self) -> Node:
        start = self.DetectLoop()
        if start == None:
            return None
        cur = start.next
        while cur.next != start:
            cur = cur.next
        cur.next = None
        return self.head
