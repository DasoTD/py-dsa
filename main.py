class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.value = value
        self.next = None
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            return True
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        
        self.length +=1

    # def pop(self):
    #     if self.length == 0:
    #         return False
    #     if self.length == 1:
    #         self.head = None
    #         self.tail = None
    #         self.length -=1

myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.print_list()
            