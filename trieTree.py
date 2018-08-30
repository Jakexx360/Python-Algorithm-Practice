# Python program for the implementation of a Trie


# Trie node class
class TrieNode:
    def __init__(self):
        # Create an empty list of the length of the alphabet
        self.children = [None] * 26

        # Value for the node
        self.value = None


# Trie data structure class
class Trie:
    def __init__(self):
        self.root = self._get_node()

    # Returns new trie node (initialized to None)
    def _get_node(self):
        return TrieNode()

    # Converts key current character into index
    # Supports only 'a' through 'z' and lower case
    def _index_char(self, ch):
        return ord(ch) - ord('a')

    # If not present, inserts key into trie
    # If the key is prefix of trie node, just marks leaf node
    def insert(self, key, value):
        curr_node = self.root
        length = len(key)

        for level in range(length):
            # Get desired index of the current character
            index = self._index_char(key[level])

            # If current character is not present
            if not curr_node.children[index]:
                # Create the child node at the desired index
                curr_node.children[index] = self._get_node()
            # Move on to the next node
            curr_node = curr_node.children[index]

        # Insert the value
        curr_node.value = value

    # Search key in the trie
    # Returns value if key present in trie, else None
    def search(self, key):
        curr_node = self.root
        length = len(key)

        for level in range(length):
            # Get desired index of the current character
            index = self._index_char(key[level])

            # If the current character does not exist in curr_node's children
            if not curr_node.children[index]:
                return None
            # Move on to the next node
            curr_node = curr_node.children[index]

        # Return the value of the last node
        return curr_node.value

    # Delete value for the given key from the trie
    # Note: Does not remove nodes that are no longer needed
    def delete(self, key):
        curr_node = self.root
        length = len(key)

        for level in range(length):
            # Get desired index of the current character
            index = self._index_char(key[level])

            # If the current character does not exist in curr_node's children
            if not curr_node.children[index]:
                # Key does not exist, return
                return
            # Move on to the next node
            curr_node = curr_node.children[index]
        # Delete the value of the last word
        curr_node.value = None


t = Trie()
keys = ["the", "a", "there", "and", "any", "by", "their"]
values = [0, 1, 2, 3, 4, 5, 6]
for k, v in zip(keys, values):
    t.insert(k, v)
print(t.search(keys[1]) == 1)  # True
print(t.search(keys[3]) == 3)  # True
print(t.search(keys[4]) == 4)  # True
t.delete(keys[4])
print(t.search(keys[4]) is None)  # True
