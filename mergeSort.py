# Performs a recursive merge-sort of the given list x. O(n*log(n))
def merge_sort(x):
    # Base case
    if len(x) < 2:
        return x

    # Create the result list
    result = []

    # Calculate the midpoint
    mid = int(len(x) / 2)

    # Recursively call merge sort on each half of the list
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])

    # While both left and right half are not empty
    while (len(left) > 0) and (len(right) > 0):

        # If first value in left is larger than the first value in right
        if left[0] > right[0]:
            # Append the first value of right to the result
            result.append(right[0])
            # And remove the value from right
            right.pop(0)

        # If first value in right is larger or equal to the first value in left
        else:
            # Append the first value of left to the result
            result.append(left[0])
            # And remove the value from left
            left.pop(0)

    # Append any remaining values in left and right to the result
    result += left
    result += right
    # Return the result
    return result


print(merge_sort([3, -5, 10, -20, -18, 5, 5]) == [-20, -18, -5, 3, 5, 5, 10])  # True
print(merge_sort([]) == [])  # True
print(merge_sort([10]) == [10])  # True
