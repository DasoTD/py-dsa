from operator import ne
import this


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
            pre = self.head
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
            self.head = None
            self.tail = None
        return temp

    def Get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

        # or

        # temp = self.head
        # while temp is not None:
        #     if temp.value == index:
        #         return temp.value
        #     temp = temp.next

    def set_value(self, index, value):
        temp = self.Get(index)
        # if temp:
        #     temp.value = value 
        #     return True

        # or 

        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)

        temp = self.Get(index - 1)
        
        
        if temp:
            new_node.next = temp.next
            temp.next = new_node
        # or
        # this cannot work because value cannot have .next except been made a Node

        # val = self.Get(index )
        # if temp:
        #     temp.next = value
        #     value.next = val
        self.length += 1
        return True

    def remove(self, index):
        if index == self.length:
            return self.pop()
        if index == 0:
            return self.pop_first()

        
        pre = self.Get(index - 1)
        # temp = self.Get(index) /// this is correct but this is 0(n)
        # this is 0(1) way to do it below it is
        temp = pre.next
        if pre:
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before =None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            # return self
        # pass 
    #     reverse(){
    #     let temp = this.head
    #     this.head = this.tail
    #     this.tail = temp
    #     let next = temp.next
    #     let prev = null
    #     for(let i =0; i< this.length; i++){
    #         next = temp.next
    #         temp.next = prev
    #         prev = temp
    #         temp = next
    #     }
    #     return this
    # }
        

 

myLinkedList = LinkedList(1)
myLinkedList.append(2)
# myLinkedList.print_list()
print(myLinkedList.Get(1))
myLinkedList.prepend(0)
myLinkedList.append(3)
# myLinkedList.pop()
# myLinkedList.print_list()
# print(myLinkedList.Get(2))
# myLinkedList.pop_first()
# myLinkedList.set_value(1,4)
# myLinkedList.print_list()
# myLinkedList.insert(3,7)
# myLinkedList.print_list()
# print(myLinkedList.remove(2))
# myLinkedList.print_list()
# myLinkedList.reverse()
# myLinkedList.print_list()
# print(myLinkedList.pop())
# myLinkedList.print_list()
# print(myLinkedList.pop())
# print(myLinkedList.pop())
            