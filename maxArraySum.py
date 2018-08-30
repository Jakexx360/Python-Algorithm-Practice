# Calculate max sum of array elements in O(n*log(n)) time
def max_array_sum(arr):
    if len(arr) == 0:
        # Empty array, return zero
        return 0
    elif len(arr) == 1:
        # Return only element in array
        return arr[0]

    # Knowing we have at least two values, sort the array
    arr.sort()  # O(nlogn)
    # Get all negatives in the array
    negatives = list(filter(lambda x: x < 0, arr))  # O(n)
    # Get all positives (and zeroes) in the array
    positives = list(filter(lambda x: x >= 0, arr))  # O(n)

    if len(positives) > 1:
        # If there are at least two positives, the max sum
        # will be the sum of the positive array
        return sum(positives)  # O(n)
    elif len(positives) == 1:
        # If there is one positive, the max sum will be the positive plus
        # the negative value closest to zero
        return positives[0] + negatives[len(negatives) - 1]  # O(1)
    else:
        # If there are no positives, the max sum will be
        # the sum of the two negatives closest to zero
        return negatives[len(negatives) - 1] + negatives[len(negatives) - 2]  # O(1)


print(max_array_sum([-10, -20, -30, -10]))  # -20
print(max_array_sum([-5, -10, -20, -30, -10, 5]))  # 0
print(max_array_sum([-10, 0, -1, 0, 1]))  # 1
print(max_array_sum([-10, -20, 0, -10]))  # -10
print(max_array_sum([-10, 10, -20, -30, -10, 5, 0, 10]))  # 25


# Calculate maximum sum of continuous subsets of the input array in O(nW) time
def max_partial_sum(arr):
    # If given an empty array, no valid max sum exists
    if len(arr) < 1:
        return "Empty input - no valid max sum"

    # Default max_sum to first value in arr
    max_sum = arr[0]
    # Default current_max_sum so far to zero
    current_max_sum = 0

    for i in arr:
        # Add arr[i] to the current_max_sum so far
        current_max_sum += i
        # If the current_max_sum so far is greater than the global max_sum,
        # set max_sum to current_max_sum
        if current_max_sum > max_sum:
            max_sum = current_max_sum
        # If the current_max_sum is less than zero,
        # reset current_max_sum to zero
        if current_max_sum < 0:
            current_max_sum = 0

    # Return the global max sum
    return max_sum


print(max_partial_sum([3, -3, 3, -1, 6, 0, 1, -1, 1, -5]))  # 9
print(max_partial_sum([]))  # Empty input - no valid max sum
print(max_partial_sum([-5]))  # -5
print(max_partial_sum([-2, -1]))  # -1
print(max_partial_sum([0, 0, -1]))  # 0
