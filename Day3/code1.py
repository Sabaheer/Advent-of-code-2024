import re

def sum_mul_instructions(corrupted_memory):
    # Regular expression to match valid mul(X,Y) patterns
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Find all matches in the corrupted memory
    matches = re.findall(pattern, corrupted_memory)
    
    # Sum the results of each multiplication
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

def read_input_file(filename):
    # Read the contents of the input file
    with open(filename, 'r') as file:
        return file.read()

# Read the corrupted memory from input.txt
input_file = 'input.txt'
corrupted_memory = read_input_file(input_file)

# Get the result
result = sum_mul_instructions(corrupted_memory)
print(result)