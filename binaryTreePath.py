# Binary Tree Node
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# Represents a Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def get_path(self, root, path, k):
        # base case handling
        if root is None:
            return False

        # append the node value in path
        path.append(root.value)

        # See if the k is same as root's data
        if root.value == k:
            return True

        # Check if k is found in left or right sub-tree
        if ((root.left is not None and self.get_path(root.left, path, k)) or
                (root.right is not None and self.get_path(root.right, path, k))):
            return True

        # If not present in subtree rooted with root,
        # remove root from path and return False
        path.pop()
        return False

    # Find minimum distance between two nodes
    def distance(self, value1, value2):
        # Get a path from root to value1
        path1 = []
        if not self.get_path(self.root, path1, value1):
            return -1

        # Get a path from root to value2
        path2 = []
        if not self.get_path(self.root, path2, value2):
            return -1

        # iterate through the paths to find the common path length
        i = 0
        while i < len(path1) and i < len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i += 1

        # get the path length by deducting the
        # intersecting path length (2 * i)
        return len(path1) + len(path2) - 2 * i


t = BinaryTree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.right.right = Node(7)
t.root.right.left = Node(6)
t.root.left.right = Node(5)
t.root.right.left.right = Node(8)
print(t.distance(8, 5) == 5)  # True
print(t.distance(2, 4) == 1)  # True
print(t.distance(2, 10) == -1)  # True
