# Given a string A consisting of n characters and a string B consisting of m characters,
# write a function that will return the number of times A must be stated such that
# B is a substring of the repeated A. If B can never be a substring, return -1.
#
# Example:
# A = ‘abcd’
# B = ‘cdabcdab’
# The function should return 3 because after stating A 3 times, getting ‘abcdabcdabcd’, B is now a substring of A.


def solution(A, B):
    accumulator = ""
    for i in range(1000):
        if B in accumulator:
            return i
        else:
            accumulator += A
    return -1


print(solution("abcd", "cdabcdab"))
print(solution("babtt", "5"))
print(solution("56657", "756657"))
