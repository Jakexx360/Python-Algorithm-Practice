# Recursively reverse a string
def reverse_string(s):
    if len(s) < 2:
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("1234") == "4321")  # True


# Maps a given function over nested list
def map_f(f, arr, result=None):
    if result is None:
        result = []

    for x in arr:
        if isinstance(x, list):
            map_f(f, x, result)
        else:
            result.append(f(x))
    return result


print(map_f(lambda x: x * x, [1, 2, [3, 4, [5]]]) == [1, 4, 9, 16, 25])  # True


# Count the number of ways to change any given amount
# Note: Not working right, counts duplicate denominations
def count_change(val, coins, count=None):
    if count is None:
        count = 0

    if val < 0 or coins is None:
        return 0
    if val == 0:
        return 1

    for c in coins:
        count += count_change(val - c, coins)

    return count


print(count_change(10, [1, 5]) == 3)


# Generate all permutations of a list recursively
def permute(arr, start=0):
    end = len(arr)

    if start == end and arr is not None:
        print(arr)  # O(n)

    for i in range(start, end):  # O(n!)
        arr[start], arr[i] = arr[i], arr[start]
        permute(arr, start + 1)
        arr[start], arr[i] = arr[i], arr[start]


permute([1, 2, 3])
