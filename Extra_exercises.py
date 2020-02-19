# What is pseudocode
# "An outline of a program, written in a form that can easily be converted into real programming."
# "Not actually but having the appearance of; pretended; "
# Clearly outlines tasks by using (Input / Processing(add/save as) / Output )
# Language independent

# Write pseudocode for a program that reads the titanic file and
# saves two other files one for the male passengers and another for the female passengers

"""
open the titanic file from its path and save as a file
loop each line in the file
    if there is a male passenger then add and append the line to a list name as male_list
    else add the line to a list name as female_list
write the output male_list into a new file and save as male.txt
write the output female_ist into a new file and save as female.txt

"""

# Creating your own functions
# Exercise 1
# Create a function called file_summary that receives a file path as a parameter (of type string)
# and returns the following string: The file <filename> has <n> lines
import sys

path = sys.argv[1]
filename = path.split("/")[-1]


def file_summary(file_path):
    count = 0
    with open(str(file_path)) as f:
        for _ in f:
            count += 1
    return count


lines = file_summary(path)
print(f"The file {filename} has {lines} lines.")


# Create a function called print_disclaimer that receives the paths of multiple files and prints:
# This program will print the summary for the following files: <filenames>

def print_disclaimer(paths):
    filenames = []
    for path in paths:
        filenames.append(path.split("/")[-1])

    return filenames


paths = sys.argv[1:]

names = print_disclaimer(paths)
print(f"This program will print the summary for the following files: {names}.")


# Exercise 2
# We’ll be using the titanic train.csv file for this exercise,
# and we’ll categorize the gender of the passengers as 0 for male and 1 for female
# In order to do that create a function called categorize_gender that receives a line of
# the titanic file as a parameter and returns 0 if the passenger is man or 1 if is a woman


def categorize_gender(row):
    row_split = row.split(',')
    if "male" in row_split:
        return row + ',0'
    else:
        return row + ',1'


with open("train.csv") as f:
    new_row_list = [f.readline().strip("\n")+',numerical_gender']
    for line in f.readlines():
        new_row = categorize_gender(line.strip("\n"))
        new_row_list.append(new_row)

    for new_line in new_row_list:
        print(new_line)
