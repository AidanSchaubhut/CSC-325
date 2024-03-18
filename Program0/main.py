# Name: Aidan Schaubuht
# Date: 3/17/24
# Decription: This is a program that takes user input, creates a singly linked list of n numbers from 0 to 100, then sorts the list

from random import randint

# Class for Nodes that will store the data for the linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None

    ##############################
    ### ACCESSORS AND MUTATORS ###
    ##############################
        
    # DATA
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    # LINK
    @property
    def link(self):
        return self._link
    
    @link.setter
    def link(self, value):
        self._link = value

    #################
    ### FUNCTIONS ###
    #################
        
    def setNext(self, link):
        self.link = link

    def __str__(self) -> str:
        return str(self.data)


# Class for linked list
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0;

    ##############################
    ### ACCESSORS AND MUTATORS ###
    ##############################

    # HEAD
    @property
    def head(self):
        return self._head
    
    @head.setter
    def head(self, value):
        self._head = value

    # TAIL
    @property
    def tail(self):
        return self._tail
    
    @tail.setter
    def tail(self, value):
        self._tail = value

    # SIZE
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        self._size = value

    #################
    ### FUNCTIONS ###
    #################
    
    # Appends a node to the end of the linked list and sets the tail to the new node
    def append(self, value):
        node = Node(value)

        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node;

        self.size += 1

    def sort(self):
        # Find the smallest, set the smallest's link to the head, set the smallest to the head
        current = self.head

        # Loop through the entire list
        while (current):
            min = current
            next = current.link

            # Loop through the unsorted list
            while (next):
                if (min.data > next.data):
                    min = next
                
                next = next.link

            # Swap the data between the nodes
            temp = current.data
            current.data = min.data
            min.data = temp
            current = current.link

    def __str__(self) -> str:
        cur = self.head
        string = ''

        while cur != None:
            string += f'{str(cur)} '
            cur = cur.link

        return string

n = input("Please, enter the number of nodes: ")
while True:
    if not (n.isnumeric()):
        n = input("Please, enter correct value for number of nodes: ")
    else:
        break
        


finalList = LinkedList()
print(f'n: {n}')
while n > 0:
    finalList.append(randint(1, 100))
    n -= 1


print(f'Unsorted list: {finalList}')
print(f'Head data: {finalList.head}')
print(f'Tail data: {finalList.tail}')
finalList.sort()
print(f'\nSorted list: {finalList}')
print(f'Head data: {finalList.head}')
print(f'Tail data: {finalList.tail}')
print('-'*30)
