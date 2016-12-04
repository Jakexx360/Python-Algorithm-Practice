# Practice Python problems solved in as few lines as possible
# Problems from: http://codingbat.com/python


# Python > List - 1 > sum3
def sum3(nums):
    return nums[0] + nums[1] + nums[2]


print("sum3: " + str(sum3([1, 2, 3])))


# Python > List - 1 > rotate_left3
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]


print("rotate_left3: " + str(rotate_left3([1, 2, 3])))


# Python > List - 1 > max_end3
def max_end3(nums):
    value = max(nums[0], nums[2])
    return [value, value, value]


print("max_end3: " + str(max_end3([5, 5, 7])))


# Python > List - 1 > make_ends
def make_ends(nums):
    return [nums[0], nums[len(nums) - 1]]


print("make_ends: " + str(make_ends([2, 7, 8, 9])))


# Python > List - 1 > has23
def has23(nums):
    return nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3


print("has23: " + str(has23([5, 7])))


# Python > List - 2 > count_events
def count_evens(nums):
    return len([x for x in nums if (x % 2) == 0])


print("count_evens: " + str(count_evens([1, 2, 3, 4, 5, 6, 7])))


# Python > List - 2 > sum13
def sum13(nums):
    nums += [0]
    return sum(x for i, x in enumerate(nums) if x != 13 and nums[i - 1] != 13)


print("sum13: " + str(sum13([1, 2, 13, 5, 7, 13])))


# Python > List - 2 > big_diff
def big_diff(nums):
    return max(nums) - min(nums)


print("big_diff: " + str(big_diff([10, 5, 15, 2, 6, 7])))


# Python > List - 2 > sum67
def sum67(nums):
    while 6 in nums:
        del nums[nums.index(6):nums.index(7, nums.index(6)) + 1]
    return sum(nums)


print("sum67: " + str(sum67([1, 2, 2, 6, 99, 99, 7, 10])))


# Python > List - 2 > centered_average
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)


print("centered_average: " + str(centered_average([1, 2, 3, 4, 100])))


# Python > List - 2 > has22
def has22(nums):
    return len([x for i, x in enumerate(nums) if (i + 1) < len(nums) and nums[i] == nums[i + 1] == 2]) > 0


print("has22: " + str(has22([1, 2, 2, 1])))


# Python > String - 1 > extra_end
def extra_end(string):
    return str(3 * string[-2:])


print("extra_end: " + extra_end('Hello'))


# Python > String - 1 > without_end
def without_end(string):
    return str(string[1:-1])


print("without_end: " + without_end('Hello'))


# Python > String - 2 > double_char
def double_char(string):
    return str("".join([x * 2 for x in string]))


print("double_char: " + double_char('Hi-There'))


# Python > String - 2 > count_code
def count_code(string):
    return len(
        [i for i in range(len(string) - 3) if string[i] == "c" and string[i + 1] == "o" and string[i + 3] == "e"])


print("count_code: " + str(count_code('cozexxcope')))


# Python > String - 2 > count_hi
def count_hi(string):
    return len([i for i in range(len(string) - 1) if string[i] == "h" and string[i + 1] == "i"])


print("count_hi: " + str(count_hi('ABChi hi')))


# Python > String - 2 > end_other
def end_other(a, b):
    return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())


print("end_other: " + str(end_other('abc', 'abXabc')))


# Python > String - 2 > cat_dog
def cat_dog(string):
    return string.count('cat') == string.count('dog')


print("cat_dog: " + str(cat_dog('1cat1cadodog')))


# Python > String - 2 > xyz_there
def xyz_there(string):
    return (string.count('xyz') - string.count('.xyz')) > 0


print("xyz_there: " + str(xyz_there('xyz.abc.xyz')))


# Count lines, words, and characters in the input string
def word_count(input_str):
    return [len(input_str.split('\n')), len(input_str.split()), len(input_str)]


input_str1 = "The quick brown fox jumped over the lazy dog.\n"
print("Word count: " + str(word_count(input_str1)))


# Count digits, whitespace, and characters
def my_count(input_str):
    count = [input_str.count(c) for c in "0123456789 \t\n"]
    return count[:10] + [sum(count[10:])] + [len(input_str) - sum(count)]


input_str2 = "The 25 quick brown foxes jumped over the 27 lazy dogs 17 times."
print("Digit count: " + str(my_count(input_str2)))
