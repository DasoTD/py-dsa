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
            # return True
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        else: 
            # pre = self.head
            temp = self.head
            while(temp.next):
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # temp = self.head
            # self.head = new_node
            # self.head.next = temp
        
        # or
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head.next = self.head
        temp.next = None
        self.length -= 1
        if self.length == 0 :
            self.tail = None
        return temp.value

 

myLinkedList = LinkedList(1)
myLinkedList.append(2)
myLinkedList.print_list()
myLinkedList.prepend(0)
myLinkedList.print_list()
myLinkedList.pop_first()
myLinkedList.print_list()
# print(myLinkedList.pop())
# myLinkedList.print_list()
# print(myLinkedList.pop())
# print(myLinkedList.pop())
            