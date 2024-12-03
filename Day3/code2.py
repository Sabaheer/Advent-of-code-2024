import re

def sum_enabled_mul_instructions(corrupted_memory):
    # Regular expression to match valid mul(X,Y) patterns
    pattern = r'mul\((\d+),(\d+)\)'
    
    # Variable to track the current status of mul instructions (enabled or disabled)
    mul_enabled = True
    total_sum = 0

    # Split the corrupted memory by instructions to handle do() and don't() separately
    instructions = re.split(r'(\bdo\(\)|\bdon\'t\(\))', corrupted_memory)
    
    for instruction in instructions:
        # Check for 'do()' or 'don't()' instructions and adjust the mul_enabled flag accordingly
        if 'do()' in instruction:
            mul_enabled = True
        elif "don't()" in instruction:
            mul_enabled = False
        elif mul_enabled:
            # If mul instructions are enabled, process the mul(X,Y) pattern in this part of the string
            matches = re.findall(pattern, instruction)
            # Multiply the numbers and add the result to the total sum
            total_sum += sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

def read_input_file(filename):
    # Read the contents of the input file
    with open(filename, 'r') as file:
        return file.read()

# Read the corrupted memory from input.txt
input_file = 'input.txt'  # Name of the input file
corrupted_memory = read_input_file(input_file)

# Get the result
result = sum_enabled_mul_instructions(corrupted_memory)
print(result)









