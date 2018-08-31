# Recursively reverse a string
def reverse_string(s):
    if len(s) < 2:
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("1234") == "4321")  # True
