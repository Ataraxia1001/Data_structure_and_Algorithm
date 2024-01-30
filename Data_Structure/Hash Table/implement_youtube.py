import pprint
# reference: https://www.youtube.com/watch?v=54iv1si4YCM&list=WL&index=69 -> there are exercises.

class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]: # search same key in linked list.
            if element[0] == key: 
                return element[1]
            
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key: # if same key is already exists, then update the value.
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found: # if same key is not exists, then append the key and value. same h makes linked list.(O(n))
            self.arr[h].append((key, val))
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        
t = HashTable()
t["march 6"] = 120
t["march 6"] = 78
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459
pp = pprint.PrettyPrinter(width=40, depth=3, compact=False)
# pp.pprint(t.arr)
print(t["march 17"])
del t["march 17"]
print(t.arr)
del t["march 6"]
print(t.arr)