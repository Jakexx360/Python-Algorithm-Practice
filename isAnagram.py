# Checks if one string is an anagram of another O(n*m)
def is_anagram(str1, str2):
    # Count letters in str1
    letters1 = dict()
    for c in str1:  # O(n)
        letters1[c] = letters1.get(c, 0) + 1  # O(1)
    # Count letters in str2
    letters2 = dict()
    for c in str2:  # O(m)
        letters2[c] = letters2.get(c, 0) + 1  # O(1)
    # Compare the letter dict
    for key, value in letters1.items():  # O(n)
        # If the values for this key are the same
        if letters2.get(key, -1) == value:  # O(1)
            # Delete the key from the second letter dict
            del letters2[key]  # O(1)
        else:
            return False
    # If second letter dict is empty, all values were equal
    return len(letters2) == 0  # O(1)


print(is_anagram("test", "ttse"))  # True
print(is_anagram("test", "tttt"))  # False
print(is_anagram("1234555", "5152534"))  # True
