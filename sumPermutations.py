# Calculate max sum of array elements in O(n*log n) time
def max_sum(arr):
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


print(max_sum([-10, -20, -30, -10]))  # -20
print(max_sum([-5, -10, -20, -30, -10, 5]))  # 0
print(max_sum([-10, 0, -1, 0, 1]))  # 1
print(max_sum([-10, -20, 0, -10]))  # -10
print(max_sum([-10, 10, -20, -30, -10, 5, 0, 10]))  # 25

