import sys

class Trie:
    def __init__(self):
        self.start = None

    class TrieNode:
        def __init__(self, item, next = None, follows = None):
            self.item = item
            self.next = next
            self.follows = follows

    def __insert(node, key):
        if len(key) == 0:
            return None

        if node == None:
            return Trie.TrieNode(key[0], None, Trie.__insert(None, key[1:]))

        if key[0] == node.item[0]:
            node.follows = Trie.__insert(node.follows, key[1:])
            return node
        
        node.next = Trie.__insert(node.next, key)
        return node
    
    def insert(self, key):
        self.start = Trie.__insert(self.start, key+"$")

    def __contains(node, key):
        
        ### WRITE YOUR CODE HERE###
        # if the key is empty then we found the word
        if len(key) == 0:
            return True
        # if the node is None then the word is not in the trie
        if node == None:
            return False
        # if the first unit of the key is equal to the first unit of the node then we go down the follows path
        if key[0] == node.item[0]:
            return Trie.__contains(node.follows, key[1:])
        # else we need to go down the next path
        return Trie.__contains(node.next, key)


        
    def __contains__(self, key):
        return Trie.__contains(self.start, key+"$")

    def __str(node, indent):
        if node == None:
            return ""

        return f"\n{indent}{str(node.item)}{Trie.__str(node.follows, indent + ' ')}{Trie.__str(node.next, indent)}"

    def __str__(self):
        return Trie.__str(self.start, "")

def main():
    words = open(sys.argv[1], "r")    
    trie = Trie()
    for line in words:
        word = line.strip()
        trie.insert(word)

    print("Misspelled words:")
        
    text = open(sys.argv[2], "r")
    for line in text:
        for word in line.split():
            word = word.lower().strip(',').strip('.')

    ### WRITE YOUR CODE HERE###
            if word not in trie:
                print(f"  {word}")

    

main()
