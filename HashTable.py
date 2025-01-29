class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self,key):
        new_hash = 0
        for letter in key:
            new_hash = (new_hash + ord(letter) * 23) % len(self.data_map)
        return new_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index] [i] [0] == key:
                    return self.data_map[index] [i] [1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i] [j] [0])
        return all_keys
    
    def item_in_common(list1, list2):
        newDict = {}
        for i in list1:
            newDict[i] = True
        for j in list2:
            if j in newDict:
                return True
        return False

mainHashTable = HashTable()

mainHashTable.set_item('item1', 45)
mainHashTable.set_item('item2', 12)
mainHashTable.set_item('item3', 36)


print(mainHashTable.keys())
mainHashTable.print_table()