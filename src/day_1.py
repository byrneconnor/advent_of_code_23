import re

class SnowProduction:
    # This Class is used to solve the advent of code problem

    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name

    def open_file_contents(self):
        # Opens a text file and returns contents in str format
        with open(self.file_path + self.file_name, 'r') as file:
            # Read the entire contents of the file
            file_contents = file.read()
        return file_contents

    def string_number_fix(self, file_contents):
        # Turns string numbers (one) to contain a digit (o1ne)

        replacements = {
            'one': 'o1ne',
            'two': 't2wo',
            'three': 't3hree',
            'four': 'f4our',
            'five': 'f5ive',
            'six': 's6ix',
            'seven': 's7even',
            'eight': 'e8ight',
            'nine': 'n9ine'
        }

        for pattern, replacement in replacements.items():
            file_contents = re.sub(pattern, replacement, file_contents)

        return file_contents

    def extract_coordinates(self, file_contents):
        # Uses extracted contents and extracts the coordinates

        # Splits up lines
        lines = file_contents.splitlines()
        # Create empty list to store coordinates
        coordinates = []

        # Process each line separately
        for line in lines:
            # Find all digits
            digits = re.findall(r'\d', line)
            # Join into a string
            digits = ''.join(digits)
            # Either find first and last digit or repeat single digit to make 2 digits
            if len(digits) >= 2:
                result = digits[0] + digits[-1]
            elif len(digits) == 1:
                result = digits + digits
            else:
                raise ValueError("Invalid input format")
            coordinates.append(int(result))
        return coordinates


# Example usage
file_path = 'C:/Users/Connor/Documents/Work related/Jobs, CVs and covering letters/Advent of code/advent_of_code_23/data/day_1/'
file_name = 'main_data.txt'

snow_production = SnowProduction(file_path=file_path, file_name=file_name)
file_contents = snow_production.open_file_contents()
clean_contents = snow_production.string_number_fix(file_contents)
coordinates = snow_production.extract_coordinates(clean_contents)
sum(coordinates)