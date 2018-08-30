import math


# Finds an element in the sorted list equal to its index in O(log n) time
def find_matching_index(input_array, offset=0):
    if len(input_array) == 0:
        # If length equals zero, no match found so return false
        return False

    # Divide and conquer the array, but also round down to 0 if len(input_array) is 1
    i = math.ceil(len(input_array) / 2) if len(input_array) > 1 else 0
    if input_array[i] == offset + i:
        # If the current element matches its index, match found so return true
        return True
    elif input_array[i] < offset + i:
        # If the current element is less than its index, recursively pass
        # the second half of the array and add to offset
        return find_matching_index(input_array[(i + 1):], offset + i)
    else:
        # If the current element is greater than its index, recursively pass
        # the first half of the array but do not add to offset
        return find_matching_index(input_array[:i], offset)


print(find_matching_index([-10, -5, 0, 3, 7]))  # True
print(find_matching_index([-10, -5, 3, 4, 7, 9]))  # False
print(find_matching_index([0, 2, 5, 8, 17]))  # True
