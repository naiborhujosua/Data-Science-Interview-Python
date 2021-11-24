# TODO: Create a letter using starting_letter.txt
"""
    Creating invitation letter by implementing file directories in python.
    using starting_letter.txt and invited_names.txt to create each invitation letter
    for each person in the invited_names.txt
"""
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_text:
            completed_text.write(new_letter)

