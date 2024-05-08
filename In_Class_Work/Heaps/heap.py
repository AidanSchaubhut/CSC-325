
DEBUG = True

class Heap():
    def __init__(self) -> None:
        self.size = 0
        self.capacity = 1
        self.data = [None]

    def getData(self):
        return self.data[:self.size]    # This slices the array with the size
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.size == 0

    def __siftUp(self, child):
        parent = (child - 1) // 2

        while (child > 0) and (self.data[child] > self.data[parent]):
            # swaps the values
            temp = self.data[child]
            self.data[child] = self.data[parent]
            self.data[parent] = temp

            if DEBUG:
                print(f"{self.data[parent]} swapped with {self.data[child]}")

            # changes the index values
            child = parent
            parent = (child - 1) // 2

    def buildFrom(self, seq):
        self.data = [None]*len(seq)
        self.size = self.capacity = len(seq)

        for x in range(self.size):
            self.data[x] = seq[x]
        
        # index is the lefft child of root
        index = (2 * self.data.index(seq[0]))

        while (index < len(seq)):
            self.__siftUp(index)
            index += 1

    def addToHeap(self, newVal):
        if (self.size == self.capacity):
            self.capacity *= 2
            temp = [None] * self.capacity
            for i in range(self.size):
                temp[i] = self.data[i]
            self.data = temp

        self.data[self.size] = newVal
        self.__siftUp(self.size)
        self.size += 1

        return newVal
    
    def __largestChild():
        pass

    def __siftDownFromTo():
        pass
    
    def sort(seq):
        h = Heap()

        # Phase I implementation
        h.buildFrom(seq)

        # Phase II Implementation
        for i in range(len(seq)):
            # take largest element and swap with smallest
            # Swapping root with very end of heap
            # ONE LINE VALUE SWAPPING AHHHHH
            h.data[0], h.data[h.size - 1] = h.data[h.size - 1], h.data[0]
            h.size -= 1                                
            h.__siftDownFromTo(0, h.size - 1)


    def __str__(self) -> str:
        st = f"\tHeap size: {(self.size)}.\n"
        st += f"\tHeap capacity: {(self.capacity)}.\n"
        st += f"\tElements in heap: \n"
        for x in range(self.size):
            st += f"\t\tValue: {(self.data[x])}\n"
        return st


def main():
    h = Heap()
    h.buildFrom([71, 15, 36, 57, 101])

    print(f"Heap is empty: {h.isEmpty()}")
    print(f"Heap size: {h.getSize()}")
    print(f"Data in heap: {h.getData()}")

    print()
    print("Heap: ")
    print(h)

    h = Heap()
    h.addToHeap(71)
    h.addToHeap(15)
    h.addToHeap(36)
    h.addToHeap(57)
    h.addToHeap(101)

    print("Heap: ")
    print(h)



main()