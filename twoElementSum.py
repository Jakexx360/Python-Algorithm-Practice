# Determine whether two elements of the given list add up to sum
def two_element_sum(arr, sum):
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    while start < end:
        curr_sum = arr[start] + arr[end]
        if curr_sum == sum:
            return True
        elif curr_sum > sum:
            end -= 1
        else:
            start += 1
    return False


print(two_element_sum([4, 7, 2, 2], 8) is False)  # True
print(two_element_sum([4, 7, 4, 3], 8))  # True
print(two_element_sum([4, 7, 2, 2, 8, 0], 8))  # True
