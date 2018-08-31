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

    # Private recursive method for checking binary search tree validity
    def _is_binary_search_tree_helper(self, current, min_val, max_val):
        if current.left is not None:
            if current.left.value < min_val \
                    or not self._is_binary_search_tree_helper(current.left, min_val, current.value):
                return False
        if current.right is not None:
            if current.right.value > max_val \
                    or not self._is_binary_search_tree_helper(current.right, current.value, max_val):
                return False
        return True

    # Returns true if this is a valid binary search tree
    def is_binary_search_tree(self):
        # Arbitrary large starting max/min values
        return self._is_binary_search_tree_helper(self.root, -100000, 100000)

    # Private recursive helper for building a path from given root to k
    def _distance_helper(self, root, path, k):
        # base case handling
        if root is None:
            return False

        # append the node value in path
        path.append(root.value)

        # See if the k is same as root's data
        if root.value == k:
            return True

        # Check if k is found in left or right sub-tree
        if ((root.left is not None and self._distance_helper(root.left, path, k)) or
                (root.right is not None and self._distance_helper(root.right, path, k))):
            return True

        # If not present in subtree rooted with root,
        # remove root from path and return False
        path.pop()
        return False

    # Returns minimum distance between two nodes with the given values
    def distance(self, value1, value2):
        # Get a path from root to value1
        path1 = []
        if not self._distance_helper(self.root, path1, value1):
            return -1

        # Get a path from root to value2
        path2 = []
        if not self._distance_helper(self.root, path2, value2):
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

    # Returns an in-order traversal of values in the tree
    def in_order(self):
        vals = []
        self._in_order_helper(self.root, vals)
        return vals

    # Private recursive helper that builds a list of node values via in-order traversal
    def _in_order_helper(self, root, values):
        if root.left is not None:
            self._in_order_helper(root.left, values)
        values.append(root.value)
        if root.right is not None:
            self._in_order_helper(root.right, values)


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
print(t.is_binary_search_tree() is False)  # True
print(t.in_order() == [4, 2, 5, 1, 6, 8, 3, 7])  # True

t = BinaryTree(5)
t.root.left = Node(3)
t.root.right = Node(7)
t.root.left.left = Node(2)
t.root.right.right = Node(8)
t.root.right.left = Node(6)
t.root.left.right = Node(4)
print(t.is_binary_search_tree())  # True
print(t.in_order() == [2, 3, 4, 5, 6, 7, 8])  # True
