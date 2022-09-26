class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None
        self.prev = None

class DoubbleLinkedList:
    def __init__(self, value) :
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.next = None
        self.prev = None
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            # print(self.tail.value)
            self.tail = new_node
        self.length +=1
        return True

myDLL = DoubbleLinkedList(4)
myDLL.print_list()
myDLL.append(3)
myDLL.print_list()
