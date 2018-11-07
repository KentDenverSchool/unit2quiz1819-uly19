#Ulysses Atkeson, 11/7/18, Tree Quiz Hashtable

class HashTable:
    def __init__(self, capacity):
        self.cap = capacity
        self.arr = [None]*self.cap
        self.pairsStores = 0 # Task 3
    def put(self, key, value):
        self.pairsStores = self.pairsStores + 1#task 3
        if self.arr[hash(key)%self.cap] == None:
            self.arr[hash(key)%self.cap] = [[key, value]] # Task 2
        else:
            self.arr[hash(key)%self.cap].append([key, value]) #Task 2
        if((1.0*self.pairsStores/self.cap) >= .8):#task 3
            self.resize(self.cap*2)#task 3
    def get(self, key):
        return self.arr[hash(key)%self.cap]
    def resize(self, newSize): #task 1
        tempArr = [None]*newSize 
        for item in self.arr:
            if item != None:
                newKey = hash(item[0][0])%newSize 
                tempArr[newKey] = item
        self.arr = tempArr
        self.cap = newSize


if __name__ == '__main__':
  h = HashTable(10)
  h.put("hi", 20)
  h.put("hi", 30)
  h.put("hello", 30)
  h.put("test", 30)
  h.put("ing", 30)
  h.put("yo", 30)
  h.put("lo", 30)
  print(h.arr)
  h.put("hey", 30)
  print(h.arr)