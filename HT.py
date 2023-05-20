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