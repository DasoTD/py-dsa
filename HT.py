# Collission happens when u insert a value to an address that already has value

# The best way to go about it is to put all data in a single address [ [a], [b]]
# it is also called separate chaining

# Another way is to search through the addresses for empty address called LINEAR PROBING


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    
    def __hash(self, key):
        my_hash =0
        for letter in key:
            my_hash = (my_hash+ ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index= self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index]= []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range (len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])

        return all_keys
    
    def items_in_common1(list1, list2):
        for i in list1:
            for j in list2:
                if i ==j:
                    return True
        return False
    def items_in_common2(list1, list2):
        my_dict = {}
        for i in list1:
            my_dict[i]= True

        for j in list2:
            if j in my_dict:
                return True
        return False



HT = HashTable()

HT.print_table()
HT.set_item("data", 1400)
HT.set_item("base", 1000)
HT.set_item("data", 1400)
HT.set_item("base", 1000)
HT.set_item("data", 1400)
HT.set_item("base", 1000)
HT.set_item("dd", 100)
HT.set_item("bb", 1040)
HT.print_table()

print(HT.get_item("basde"))

print(HT.keys())