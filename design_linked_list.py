"""
Ques. Design Linked List
T.C. = addAtHead - O(1). For the rest of the operations, it is O(n)
S.C. = O(n)  
Link - https://leetcode.com/problems/design-linked-list/
"""
class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None 

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cnt = 0
        cur = self.head 
        while cur != None:
            if(cnt == index):
                return cur.val
            cur = cur.next 
            cnt += 1
        return -1 
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if(self.head == None):
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head 
            self.head = new_node     

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if(self.head == None):
            self.head = Node(val)
        else:
            cur = self.head 
            while cur.next != None:
                cur = cur.next 

            cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if(index == 0):
            new_node = Node(val)
            new_node.next = self.head 
            self.head = new_node 
        else:
            cnt = 0
            cur = self.head
            prev = None 

            while cur != None:
                if(cnt == index):
                    new_node = Node(val)
                    new_node.next = cur 
                    prev.next = new_node
                    return 
                else:
                    prev = cur 
                    cur = cur.next
                    cnt += 1
                    
            if(cnt == index):
                cur = Node(val)
                prev.next = cur 
            
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if(index == 0):
            self.head = self.head.next
        else:
            prev = None 
            cur = self.head 
            cnt = 0 
            
            while cur != None:
                if(cnt == index):
                    next_node = cur.next
                    prev.next = next_node 
                    return
                else:
                    prev = cur 
                    cur = cur.next
                    cnt += 1 

