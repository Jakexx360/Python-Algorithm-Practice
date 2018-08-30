# A naive recursive implementation of 0-1 Knapsack Problem


# Returns the maximum value that can be put in a knapsack of given capacity
def knapsack(capacity, weights, values, num_items):
    # Base Case
    if num_items == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if weights[num_items - 1] > capacity:
        return knapsack(capacity, weights, values, num_items - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(values[num_items - 1] + knapsack(capacity - weights[num_items - 1], weights, values, num_items - 1),
                   knapsack(capacity, weights, values, num_items - 1))


print(knapsack(50, [10, 20, 30], [60, 100, 120], 3) == 220)  # True
print(knapsack(30, [10, 20, 30], [60, 100, 120], 3) == 160)  # True
