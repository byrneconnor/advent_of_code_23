import re

# Open text file
with open('C:/Users/Connor/Documents/Work related/Jobs, CVs and covering letters/Advent of code/advent_of_code_23/day_1/test.txt', 'r') as file:
    # Read the entire contents of the file
    file_contents = file.read()

file_contents

lines = file_contents.splitlines()

my_list = []

# Process each line separately
for line in lines:
    digits = re.findall(r'\d', line)
    digits = ''.join(digits)
    if len(digits) >= 2:
        result = digits[0] + digits[-1]
    elif len(digits) == 1:
        result = digits + digits
    else:
        print("Error")
    my_list.append(int(result))

sum(my_list)