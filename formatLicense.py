# Given a non-empty string S consisting of N characters representing a license key to format,
# and an integer K (the desired number of characters between dashes), returns the license key formatted properly.
# Note, the first group may be of variable length.
# For example, given S = "2-4A0r7-4k" and K = 4, the function should return "24A0-R74K",
# and for K = 3, the function should return "24-A0R-74K" as the first group could be shorter.
# Given S = "r" and K = 1, the function should return "R".


# Perform the above from front-to-back O(n)
def format_license_front(S, K):
    # Capitalize and remove hyphens
    S = S.replace("-", "").upper()  # O(n)
    # Calculate the size of the first group
    first_size = len(S) % K  # O(1)

    i = 0
    result = ""
    for c in S:  # O(n)
        # If first group or appropriate group size, insert hyphen
        if i != 0 and (i == first_size or (i - first_size) % K == 0):  # O(1)
            result += "-"
        # Append the character and increment
        result += c
        i += 1
    return result


# Perform the above from back-to-front O(n)
def format_license_back(S, K):
    # Capitalize and remove hyphens
    S = S.replace("-", "").upper()  # O(n)

    # Reverse the input string and build the result
    result = ""
    counter = 0
    for c in S[::-1]:  # O(n)
        # If the counter has reached the desired size
        if counter == K:  # O(1)
            # Append a hyphen and reset the counter
            result += "-"
            counter = 0
        # Append the character to result and increment counter
        result += c
        counter += 1
    # Reverse and return the result
    return result[::-1]  # O(n)


print(format_license_front("ggdfgg-hhhhy", 6) == format_license_back("ggdfgg-hhhhy", 6))
print(format_license_front("gggg", 3) == format_license_back("gggg", 3))
print(format_license_front("r", 1) == format_license_back("r", 1))
print(format_license_front("2-4A0r7-4k", 4) == format_license_back("2-4A0r7-4k", 4))
