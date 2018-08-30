# Print two arrays with equal sums if they exist in O(n*log(n)) time
def make_it_zero(input_array):
    arr = sorted(input_array)  # O(n*log(n))
    n = len(arr) - 1

    # Last element
    counter1 = arr[n]
    # Second to last element
    counter2 = arr[n - 1]

    # Create the two arrays
    sum1 = [counter1]
    sum2 = [counter2]

    # Starting at third to last element
    i = n - 2
    while i >= 0:  # O(n)
        if counter1 > counter2:
            counter2 = counter2 + arr[i]
            sum2.append(arr[i])
        else:
            counter1 = counter1 + arr[i]
            sum1.append(arr[i])
        i -= 1
    if counter1 != counter2:
        return [], []
    else:
        return sum1, sum2


print(make_it_zero([6, 12, 18]) == ([18], [12, 6]))  # True
print(make_it_zero([6, 1, 12]) == ([], []))  # True

# # Attempt to change signs in an array to make the sum equal to zero
# def make_it_zero(arr):
#     n = len(arr)
#     my_sum = sum(arr)  # O(n)
#
#     # Initialize the 2D array for tracking solutions O(nL)
#     subset = [[0 for x in range(n + 1)] for x in range(my_sum + 1)]
#     for i in range(n + 1):
#         # If sum is 0 -> true
#         subset[0][i] = True
#     for i in range(my_sum + 1):
#         # If sum is not 0 -> false
#         subset[i][0] = False
#
#     # Fill the subset 2D array of results O(nL)
#     i = 1
#     while i <= my_sum:  # O(L)
#         j = 1
#         while j <= n:  # * O(n)
#             subset[i][j] = subset[i][j-1]
#             if i >= arr[j-1]:
#                 subset[i][j] = subset[i][j] or subset[i-arr[j-1]][j-1]
#             j += 1
#         i += 1
#
#     # Keep track of minimum difference in sum of two subsets
#     from math import inf
#     my_min = +inf
#
#     # Fill output array keeping track of powers of -1 O(nL)
#     output_array = [0 for x in arr]
#     i = 1
#     while i <= my_sum:  # O(m)
#         j = 1
#         while j <= n:  # * O(n)
#             # If there is s subset with sum i, then check if the
#             # difference between overall sum and twice this sum is least or not.
#             # If yes update the min
#             if subset[i][j]:
#                 if abs(my_sum - 2 * i) < my_min:
#                     my_min = abs(my_sum - 2 * i)
#             if i - arr[j - 1] != 0 and subset[i][j]:
#                 output_array[j-1] = -1
#             j += 1
#         i += 1
#     if my_min == 0:
#         # If the two subsets cancel out, print output array
#         print(output_array)
#     else:
#         # If the two subsets do not cancel, print the difference between the two subsets
#         print("Cannot make the sum of array zero. Minimum offset will be: " + str(my_min))
#
# make_it_zero([5, 6, 13])  # Cannot make the sum of array zero. Minimum offset will be: 2
# make_it_zero([10, 16, 5, 5, 8, 8])  # [0, 0, -1, -1, -1, -1]
# make_it_zero([0, 1, 1])  # [0, 0, -1]
