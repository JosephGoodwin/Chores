import csv
import pygame
from datetime import date


# Function that reads the text file.
# Also gets the day of the week.
def readFile():
    day = str(date.today().weekday())
    with open('chore_list.txt', 'r') as file:
        read_line = csv.reader(file, delimiter=';')
        # Using csv it can read files in csv format.
        # Row0 is expected to be the day number in the .txt file.
        for row in read_line:
            day_num = row[0]
            day_of_week = row[1]
            tasks = row[2]
            if day_num == day:
                print(f"Today is {day_of_week}. So the chores are as follows:\n{tasks}")


# A quick way to call and test the function.
readFile()
