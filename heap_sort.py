# Heap implementation with sorting.

# Heap Sort Algorithm for sorting in increasing order:
# 1. Build a max heap from the input data.
# 2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap
# followed by reducing the size of heap by 1. Finally, heapify the root of the tree.
# 3. Repeat step 2 while size of heap is greater than 1.


class Heap:

    def __init__(self, heap=[]):
        self.heap = heap

    def heapify(self, size, node):
        """
        If node is smaller to it's left or right child then it will replace it with that child and then again call this
        function to heapify that node.

        e.g- If you replace root with left child then you have to heapify that left child (now having roo element)
        with it's further child node to move it to last position.
        """
        # left node would be 2*n if we consider first element is at position 1 instead of 0, else 2*n + 1 => with 0.
        lef_node = 2 * node + 1
        right_node = 2 * node + 2
        largest = node

        if lef_node < size and self.heap[largest] < self.heap[lef_node]:
            largest = lef_node

        if right_node < size and self.heap[largest] < self.heap[right_node]:
            largest = right_node

        if largest != node:
            self.heap[largest] , self.heap[node] = self.heap[node] , self.heap[largest]
            self.heapify(size, largest)

    def sort(self):

        # In[19]: list(range(3, 0, -1))
        # Out[19]: [3, 2, 1]

        size = len(self.heap)
        # before we start deletion, or putting it at last position, will have to create a MAX heap.
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(size, i)
        # If you will create below heap (BT) on paper, it would be max heap.
        self.print_heap()

        # Deletion in heap - remove root element - which can be achieved by moving greatest element from 1st
        # position to last position and then reducing the size of the array.
        # It's like a deletion behaviour as we are moving it to last position and also reducing the size of array.
        # So once all element is processed heap will be sorted.

        for i in range((size - 1), 0, -1):
            # it will replace first bigger element with last element
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            # so now smaller element is at root so will heapify it to move it to leaf position with reduced size.
            self.heapify(i, 0)
        return self.heap

    def create_max_heap(self, val):
        self.heap.append(val)
        size = len(self.heap)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(size, i)

    def print_heap(self):
        print ("Current heap..", self.heap)


# heap = Heap([1, 4, 6, 8, 5, 2])
# heap = Heap([1, 4, 6, 8, 5, 2, 12, 34, 56, 32, 87, 34, 99, 26])
# heap.sort()
heap = Heap()
heap.create_max_heap(1)
heap.create_max_heap(4)
heap.create_max_heap(6)
heap.create_max_heap(8)
heap.create_max_heap(5)
heap.create_max_heap(2)
heap.print_heap()

# O/P- Current heap.. [8, 6, 4, 1, 5, 2]
