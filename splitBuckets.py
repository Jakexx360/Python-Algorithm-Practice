import sys

# Splits array of int from input text file into given number of buckets (subsets).
# The buckets will be ordered and the goal is for buckets to be of minimum size.
# Outputs the created buckets to a text file.

# Verify the input and output command line arguments exist
if len(sys.argv) != 3:
    print("Error: Please provide input file and output file as arguments.")
    sys.exit()

# Read in the input file (arg[1]) and split each line into a list of strings
# NOTE: Raises IOError if the input file does not exist
# NOTE: Assuming one integer per line, e.g. properly formatted input
lines = open(sys.argv[1]).read().splitlines()

# Verify number of buckets is specified and there is at least one input number
if len(lines) < 2:
    print("Error: Please provide input file with at least one number.")
    sys.exit()

# Record the desired number of buckets
numBuckets = int(lines[0])

# Verify we are splitting the input into at least one bucket, otherwise do nothing
if numBuckets > 0:
    # Remove first item from the input list then sort the list by the int values
    lines = sorted(lines[1::], key=lambda x: int(x))
    # Divide the input size by numBuckets to determine the max number of elements that can be in each bucket
    numElements = len(lines) / float(numBuckets)

    # Split the sorted list into the given number of buckets with numElements items per bucket
    # NOTE: Assumes we don't have to fill the buckets sequentially
    buckets = [lines[int(round(numElements * i)): int(round(numElements * (i + 1)))] for i in range(numBuckets)]

    # Create/overwrite the given output file for writing the output
    with open(sys.argv[2], 'w+') as f:
        for bucket in buckets:
            f.write(" ".join(bucket) + "\n")
