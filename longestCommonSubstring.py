# Determine the length of the longest common substring of two strings and return it in O(m*n) time
def longest_common_substring(str1, str2):
    # Initialize 2D array of results O(m*n)
    results = [[0 for x in range(len(str2) + 1)] for x in range(len(str1) + 1)]
    # Find the length of the longest common substring O(m*n)
    i = 1
    while i <= len(str1):  # O(m)
        j = 1
        while j <= len(str2):  # * O(n)
            if str1[i-1] == str2[j-1]:
                # If characters are equal, add one to result
                # and continue to next character in each string
                results[i][j] = results[i-1][j-1] + 1
            else:
                # Characters are not equal, set the result to zero
                results[i][j] = 0
            j += 1
        i += 1
    # Traverse the 2D array to find the largest result O(m*n)
    result = 0
    x = 0
    i = 1
    while i <= len(str1):  # O(m)
        j = 1
        while j <= len(str2):  # * O(n)
            if result < results[i][j]:
                result = results[i][j]
                x = j
            j += 1
        i += 1
    # Return number of matching characters and those characters
    return result, str2[x - result:x]

print(longest_common_substring("my algorithms class", "algo dog cat test class"))  # 6
print(longest_common_substring("cat", "dog"))  # 0
print(longest_common_substring("cat", "bar"))  # 1
print(longest_common_substring("", "cat"))  # 0
