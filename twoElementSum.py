# Find all unique pairs of numbers in a given list that add up to the given value
def find_sum_in_list(array, value):  # O(n^2)
    results = []
    for i, x in enumerate(array):
        for j, y in enumerate(array):
            if j > i and x + y == value:
                results.append((x, y))
    return results


print(find_sum_in_list([3, 10, 13, 8, 4, 7, 21, 0], 21) == [(13, 8), (21, 0)])  # True


# Determine whether two elements of the given list add up to the given value
def two_element_sum(arr, value):  # O(n*log(n))
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    while start < end:
        curr_sum = arr[start] + arr[end]
        if curr_sum == value:
            return True
        elif curr_sum > value:
            end -= 1
        else:
            start += 1
    return False


print(two_element_sum([4, 7, 2, 2], 8) is False)  # True
print(two_element_sum([4, 7, 4, 3], 8))  # True
print(two_element_sum([4, 7, 2, 2, 8, 0], 8))  # True
