class HashSet:
    def __init__(self, contents=[]) -> None:
        self.items = [None] * 10
        self.numItems = 0

        for item in contents:
            self.add(item)

    def __add(item, items):
        # Find the index for the value beinig added to the list
        index = hash(item) % len(items)
        # Create a temp location for the value being added
        location = -1
        # Loop through the list until we find an empty spot to input the value
        while items[index] != None:
            # This check makes sure that we don't input a duplicate value
            if items[index] == item:
                return False
            # If we run into a placeholder then set the location to that index
            if(location < 0) and (type(items[index]) == HashSet.__Placeholder):
                location = index
            # Move to the next index
            index = (index + 1) % len(items)
        # If the original index hit a None value then set the location to that index
        if location < 0:
            location = index
        # And place the value
        items[location] = item

        return True
    
    def __rehash(oldList, newList):
        for x in oldList:
            if (x != None) and (type(x) != HashSet.__PlaceHolder):
                HashSet.__add(x, newList)
        return newList
    
    def add(self, item):
        if HashSet.__add(item, self.items):  # If True then the values was inserted. False, it was not
            self.numItems += 1  # Add 1 to the list size
            load = self.numItems / len(self.items)  # Check the load factor
            if load >= 0.75:    # If the load is greater than 75%
                self.items = HashSet.__rehash(self.items, [None] * 2 * len(self.items)) # Rehash the list into a new list with double the size

    class __PlaceHolder:
        def __init__(self) -> None:
            pass
        def __eq__(self, other):
            return False

    def __remove(item, items):
        index = hash(item) % len(items)

        while items[index] != None:
            if items[index] == item:
                nextIndex = (index + 1) % len(items)

                if items[nextIndex] == None:
                    items[index] = None
                else:
                    items[index] = HashSet.__PlaceHolder()
                
                return True
            index = (index + 1) % len(items)
        return False
    
    def remove(self ,item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)

            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None] * int(len(self.items) / 2))
        else:
            raise KeyError("Item not in HashSet")
        
    def discard(self, item):
        if HashSet.__remove(item, self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)

            if load <= 0.25:
                self.items = HashSet.__rehash(self.items, [None] * int(len(self.items) / 2))

    # Overrides the 'in' operator
    def __contains__(self, item):
        index = hash(item) % len(self.items)

        while self.items[index] !=  None:
            if self.items[index] == item:
                return True
            index = (index + 1) % len(self.items)

        return False
    
    def __iter__(self):
        for i in range(len(self.items)):
            if (self.items[i] != None) and (type(self.items[i]) != HashSet.__PlaceHolder):
                yield self.items[i]

    # A - B
    # A = {10, 20, 30, 40, 80}
    # B = {100, 30, 80, 40, 60}
    # C = A - B = {10, 20}
    # C = B - A = {100, 60}
                
    def difference_update(self, other):  # A.difference_update(B) -> A = A - B
        for item in other: # B = other
            self.discard(item)  # A.discard(item)
        
    def difference(self, other): # A.difference(B) -> C = A - B
        result = HashSet(self)
        result.difference_update(other)
        return result
    
    def issuperset(self, other):
        for item in other:
            if item not in self:
                return False
        return True
    
    def clear(self):
        self.numItems = 0
        self.items = [None] * 10

    def update(self, other):
        for item in other:
            self.add(item)

    def __len__(self):
        return self.numItems