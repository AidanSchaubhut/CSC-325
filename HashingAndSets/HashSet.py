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

    def __contains__(self, item):
        index = hash(item) % len(self.items)

        while self.items[index] !=  None:
            if self.items[index] == item:
                return True
            index = (index + 1) % len(self.items)

        return False
    
    def __iter__(self):
        pass

hash_set = HashSet([1,2,3,4,4,5,5,6,7,10,12,15,15])


print(23 in hash_set)