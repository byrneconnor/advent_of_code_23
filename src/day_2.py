import re

class ElfGame:

    def __init__(self, input_location):
        self.input_location = input_location

    def import_txt(self):
        # Open txt file and convert to list
        with open(self.input_location, 'r') as file:
            # Read the entire contents of the file
            file_contents = file.read()
        return file_contents

    def convert_to_dict(self, input_str):  # Added 'self' as the first parameter
        games_dict = {}

        # Split the input string into individual games
        game_strings = input_str.strip().split('\n')

        for game_str in game_strings:
            # Extract game number and content
            match = re.match(r'Game (\d+): (.+)', game_str)
            if match:
                game_number, game_content = match.groups()

                # Split the game content into color-quantity pairs
                color_quantity_pairs = re.findall(r'(\d+)\s*([a-zA-Z]+)', game_content)

                # Create a dictionary to store quantities for each color
                color_dict = {}
                for quantity, color in color_quantity_pairs:
                    color_dict[color] = color_dict.get(color, []) + [int(quantity)]

                # Add the color dictionary to the games dictionary
                games_dict[game_number] = color_dict

        return games_dict

# File path
file_name = 'game_data.txt'
input_location = 'C:/Users/Connor/Documents/Work related/Jobs, CVs and covering letters/Advent of code/advent_of_code_23/data/day_2/' + file_name

# Create ElfGame instance
elf_game = ElfGame(input_location)

# Import and convert data
input_data = elf_game.import_txt()
result_dict = elf_game.convert_to_dict(input_data)

# Print the result
print(result_dict)

red_limit = 12
green_limit = 13
blue_limit = 14


filtered_ids = [int(key) for key, value in result_dict.items() if ('red' in value and max(value['red']) <= red_limit)
                and ('green' in value and max(value['green']) <= green_limit)
                and ('blue' in value and max(value['blue']) <= blue_limit)]

sum(filtered_ids)
