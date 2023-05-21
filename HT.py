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

def find_duplicates(nums):
    nums_count = {}
    for num in nums:
        nums_count[num] = nums_count.get(num, 0)+1
        # print(nums_count[num])
    duplicates = [num for num, count in nums_count.items() if count > 1]
    return duplicates

def first_non_repeating_char(string):
    string_count = {}

    for char in string:
        string_count[char] =string_count.get(char,0)+1
    
    for char in string:
        if string_count[char] ==1:
            return char

def group_anagrams(strings):
    anagram_group = {}
    for string in strings:
        cannonical = ''.join(sorted(string))
        if cannonical in anagram_group:
            anagram_group[cannonical].append(string)
        else:
            anagram_group[cannonical] = [string]
    
    return list(anagram_group.values())


def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
    
    
    
    
print ( two_sum([2, 7, 11, 15], 9) )

# HT = HashTable()

# HT.print_table()
# HT.set_item("data", 1400)
# HT.set_item("base", 1000)
# HT.set_item("data", 1400)
# HT.set_item("base", 1000)
# HT.set_item("data", 1400)
# HT.set_item("base", 1000)
# HT.set_item("dd", 100)
# HT.set_item("bb", 1040)
# HT.print_table()

# print(HT.get_item("basde"))

# print(HT.keys())

# print ( find_duplicates([1, 2, 3, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 3]) )
# print ( find_duplicates([1, 1, 1, 1, 1]) )
# print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
# print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
# print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3,2]) )
# print ( find_duplicates([]) )

print(first_non_repeating_char("lleetcode"))
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )