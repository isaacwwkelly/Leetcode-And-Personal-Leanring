# Knapsack Problem
# Use dynamic programming (make a grid), where the cells are the answer to sub problems (smaller knapsacks with smaller weight carrying capacity)

# We are a theif trying to maximize the value of stolen items, while not exceeding the weight capacity of the knapsack
# Dynamic Programming is all about breaking down a problem into subproblems, and then using the answers to those subproblems to solve the original problem
# So what's the main problem? To answer that, we have to identify the CONSTRAINT. In this case, the constraint is the weight capacity of the knapsack
# Now that we know the constraint, we can break the problem down into subproblems, which is a smaller knapsack with a smaller weight capacity
# This will look like a grid, where each row is an item, and each column is a weight capacity (see notes for illustration)

def combine_two_knapsacks(knap1, knap2):
    first = knap1[0] + knap2[0]
    second = (knap1[1] if knap1[1] is not None else []) + (knap2[1] if knap2[1] is not None else [])
    return (first, second)

def knapsack(items, capacity):

    # let's make a grid to store the answers to the subproblems
    grid = [[(0, None)] * capacity for i in range(len(items))]

    # go row by row
    item_index = 0
    for item__key, item_stats in items.items():

        # go column by column
        for weight_capacity in range(1, capacity + 1):
            weight_index = weight_capacity - 1

            # Get the max value for thi current cell at grid[item_index][weight_index]
            # This could be the previous cell, which is above this cell (at grid[item_index - 1][weight_index]), 
            # or it could be the current item + the prvious row's cell that can fit in the remaining weight capacity after adding the current item to the knapsack: [the current item + what we can get with the remaining weight_index (at grid[item - 1][weight_index - item_stats["weight"]])]

            cell_above = grid[item_index - 1][weight_index] if item_index > 0 else (0, None)
            remaining_weight_cell = grid[item_index - 1][weight_index - item_stats["weight"]] if (item_index > 0 and weight_index - item_stats["weight"] >= 0) else (0, None)

            # check if the current knapsack can even fit the current item, or if the cell above's value is better than the current item's value + value of remaining weight
            if (item_stats["weight"] > weight_capacity) or (cell_above[0] >= item_stats["value"] + remaining_weight_cell[0]):
                grid[item_index][weight_index] = cell_above
            
            else:
                # if there is carrying capacity for the current item and more, then add the current item and the previous cell at weight_index - item_stats["weight"]
                grid[item_index][weight_index] = combine_two_knapsacks((item_stats["value"], [item__key]), remaining_weight_cell)           
            
        item_index += 1

    return grid


items = {
    "guitar": {"weight": 1, "value": 1500},
    "sterio": {"weight": 4, "value": 3000},
    "laptop": {"weight": 3, "value": 2000},
    "phone": {"weight": 1, "value": 2000},
    "keyboard": {"weight": 1, "value": 1000},
}
capacity = 4

# print("\nKnapsack Problem")
# result = knapsack(items, capacity)
# print(result[-1][-1])


# Longest Common Substring Problem
# Given two strings, find the longest common substring between the two strings
# If given "fish" and "hish", the longest common common substring is "ish"

def longest_common_substring(s1, s2):
    grid = [[(0, "")] * (len(s2) + 1) for i in range(len(s1) + 1)]

    max_length = 0
    longest_common_substring = ""

    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]: # if the characters are equal, then this grid's cell is 1 + the cell above and to the left's value
                if i == 0 or j == 0: # if the previous cell is out of bounds, just set it to 1
                    grid[i][j] = (1, s1[i])
                else:
                    grid[i][j] = (grid[i-1][j-1][0] + 1, grid[i-1][j-1][1] + s1[i])
                
                if grid[i][j][0] > max_length:
                    max_length = grid[i][j][0]
                    longest_common_substring = grid[i][j][1]

    return max_length, longest_common_substring

print("\nLongest Common Substring Problem")
result = longest_common_substring("fish", "hish")
print(f"LCS('fish', 'hish') --> {result}")


# Longest Common Subsequence Problem
# Given two strings, find the longest common subsequence between the two strings
# If given "fish" and "foosh", the longest common subsequence is "fsh" because both strings have "f", "s", and "h" in order. There may be chars between the "f", "s", and "h", but it doesn't matter in a longest common subsequence

def longest_common_subsequence(s1, s2):
    grid = [[(0, "")] * (len(s2)) for i in range(len(s1))]

    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            
            # if the characters are equal, then this grid's cell is 1 + the cell above and to the left's value
            if s1[i] == s2[j]:
                # check if the previous cell is out of bounds, just set it to 1
                if i == 0 or j == 0:
                    grid[i][j] = (1, s1[i])
                else:
                    grid[i][j] = (grid[i-1][j-1][0] + 1, grid[i-1][j-1][1] + s1[i])


            # if the characters are not equal, then this grid's cell is the max of the cell above and the cell to the left
            else:
                grid[i][j] = max(grid[i][j-1], grid[i-1][j])

    return grid[-1][-1]

print("\nLongest Common Subsequence Problem")
result = longest_common_subsequence("fish", "foosh")
print(f"LCSS('fish', 'foosh') --> {result}")