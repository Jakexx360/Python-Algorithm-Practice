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
