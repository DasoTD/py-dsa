# linked list around a given value.
import math
 
# Link list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
# A utility function to create a new node
class LinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.data = data
        self.next = None
        return new_node
        # self.head = new_node
        # self.tail = new_node
        # self.length = 1

def newNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    return new_node
 
# Function to make a new list
# (using the existing nodes)
# and return head of new list.
def partition(head, x):
     
    # Let us initialize start and
    # tail nodes of new list
    tail = head
 
    # Now iterate original list
    # and connect nodes
    curr = head
    while (curr != None):
        next = curr.next
        if (curr.data < x):
             
            # Insert node at head.
            curr.next = head
            head = curr
         
        else:
             
            # Append to the list of greater values
            # Insert node at tail.
            tail.next = curr
            tail = curr
         
        curr = next
     
    tail.next = None
 
    # The head has changed, so we need
    # to return it to the user.
    return head
 
# Function to print linked list
def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end = " ")
        temp = temp.next
     
# Driver Code
if __name__=='__main__':
     
    # Start with the empty list
    head = newNode(3)
    head.next = newNode(5)
    head.next.next = newNode(8)
    head.next.next.next = newNode(2)
    head.next.next.next.next = newNode(10)
    head.next.next.next.next.next = newNode(2)
    head.next.next.next.next.next.next = newNode(1)
 
    x = 5
    head = partition(head, x)
    printList(head)
     
# This code is contributed by AbhiThakur