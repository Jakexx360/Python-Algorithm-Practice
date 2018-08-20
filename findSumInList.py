# Find all pairs of numbers in a given list that add up to a given value
def find_sum_in_list(array, value):
    results = []
    for i, x in enumerate(array):
        for j, y in enumerate(array):
            if j != i and x + y == value:
                results.append((x, y))
    return results


print(find_sum_in_list([3, 10, 13, 8, 4, 7, 21, 0], 21))
