# Hash Map implementation with list and linked list.


class KeyValueNode:
    def __init__(self, key=None, val=None):
        self.val = val
        self.key = key
        self.next = None


class KeyValueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def add(self, key, val):
        node = KeyValueNode(key, val)
        if not self.front:
            self.front = node
            self.rear = node
            return True
        self.rear.next = node
        self.rear = node

    def get_value(self, key):
        front = self.front
        while front:
            if front.key == key:
                return front.val
            front = front.next

    def print_queue(self):
        front = self.front
        while front:
            print(front.key, front.val, end='  ')
            front = front.next
        print("\n")


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_index = [0]*self.size

    @staticmethod
    def generate_hash(val):
        return val%10

    def add(self, key, val):
        hash_value = self.generate_hash(key)
        if self.hash_index[hash_value] == 0:
            self.hash_index[hash_value] = KeyValueLinkedList()
        self.hash_index[hash_value].add(key, val)

    def get_value(self, key):
        hash_value = self.generate_hash(key)
        if self.hash_index.__contains__(hash_value):
            return self.hash_index[hash_value].get_value(key)
        return False


    def print_hash_table(self):
        for node in self.hash_index:
            if node:
                node.print_queue()

ht = HashTable(20)
ht.add(4, 'A4')
ht.add(14, 'A14')
ht.add(8, 'B')
ht.add(10, 'C10')
ht.add(20, 'C20')
ht.print_hash_table()
print("Fetching value {}.".format(10), ht.get_value(10))

"""
Output:
10 C10  20 C20  

4 A4  14 A14  

8 B  

Fetching value 10. C10
"""
