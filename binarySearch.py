# Given a sorted array arr and a value x to locate, returns location of x if present, else returns -1. O(log(n))
def binary_search(arr, x):
    # Set boundaries of search
    lower = 0
    upper = len(arr) - 1

    # Iterate over array
    while lower <= upper:  # O(log(n))
        # Calculate midpoint
        mid = lower + (upper - lower) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            lower = mid + 1

        # If x is smaller, ignore right half
        else:
            upper = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


print(binary_search([1, 2, 4, 6, 8, 10], 6) == 3)
print(binary_search([1, 2, 4, 6, 8, 10], 1) == 0)
print(binary_search([1, 2, 4, 6, 8, 10], 10) == 5)
print(binary_search([1, 2, 4, 6, 8, 10], 3) == -1)
