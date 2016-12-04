# Remove duplicates from an array in O(n*log n) time
def remove_duplicates(input_array):
    # Sort the input array
    sorted_array = sorted(input_array)  # O(nlogn)
    # Create array that will contain unique sorted elements of input_array
    sorted_output = []

    i = 0
    while i < len(sorted_array):  # O(n), each element is only traversed once
        offset = 1

        # Copy the element to the output array
        sorted_output.append(sorted_array[i])

        # While the next element is equal to this element, add to offset
        while i + offset < len(sorted_array) and sorted_array[i] == sorted_array[i + offset]:
            i += 1

        # Add offset to i which skips all the duplicate elements
        i += offset

    # Create hash map / dictionary to add unique values of sorted_output to
    output_map = {}
    for element in sorted_output:  # O(n)
        output_map.update({element: element})

    # Create array that will contain sorted_output with the original array order
    output_array = []
    i = 0
    for element in input_array:  # O(n)
        if element in output_map:  # O(1)
            output_array.append(element)
            del output_map[element]  # O(1)
            i += 1
    return output_array


print(remove_duplicates([4, 5, 5, 4, 6, 7, 8, 5, 5, 7, 12, 0]))  # output: [4, 5, 6, 7, 8, 12, 0]
