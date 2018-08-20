# given a non-empty string S consisting of N characters,
# representing a license key to format, and an integer K,
# returns the license key formatted according to the description above.
# For example, given S = "2-4A0r7-4k" and K = 4, the function should return "24A0-R74K",
# and for K = 3, the function should return "24-A0R-74K" as the first group could be shorter.
# Given S = "r" and K = 1, the function should return "R".

def solution(S, K):
    # Capitalize and remove hyphens
    S = S.upper().strip("-")
    first_size = len(S) % K

    i = 0
    result = ""
    for c in S:
        # If first group or appropriate group size, insert hyphen
        if i != 0 and (i == first_size or (i - first_size) % K == 0):
            result += "-"
        # Append the character and increment
        result += c
        i += 1
    return result


print(solution("ggdfgg-hhhhy", 6))
print(solution("gggg", 3))
