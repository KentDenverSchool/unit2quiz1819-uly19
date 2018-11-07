#Ulysses Atkeson, 11/7/18, Tree Quiz Hashtable
import unittest
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

class TestMethods(unittest.TestCase):
    def test_init(self):#
        print("Running init test")
        h = HashTable(1000)
        self.assertEqual(h.get("0"), None)
        print("init test complete\n")

    def test_put_and_get(self):
        print("Running put and get test")
        h = HashTable(1000)
        self.assertEqual(h.get("test"), None)
        h.put("test", "ing")
        h.put("do", "thing")
        self.assertEqual(h.get("test"), [["test","ing"]])
        self.assertEqual(h.get("idk"), None)
        print("put and get test complete\n")

    def test_task1(self):
        print("Running task 1 test")
        h = HashTable(10)
        h.put("test", 1)
        h.resize(20)
        self.assertEqual(h.get("test"), [["test", 1]])
        h.resize(1)
        self.assertEqual(h.get("test"), [["test", 1]])
        print("task 1 test complete\n")

    def test_task2(self):
        print("Running task 2 test")
        h = HashTable(10)
        h.put("test", 1)
        h.put("test", 2)
        self.assertEqual(h.get("test"), [["test", 1], ["test", 2]])
        print("task 2 test complete\n")
    
    def test_task3(self):
        print("Running task 3 test")
        h = HashTable(5)
        h.put("test", 1)
        h.put("ing", 2)
        h.put("hey", 3)
        self.assertEqual(h.cap, 5)
        h.put("troll", 4)
        self.assertEqual(h.cap, 10)
        print("task 3 test complete\n")

if __name__ == '__main__':
  unittest.main()#task 4