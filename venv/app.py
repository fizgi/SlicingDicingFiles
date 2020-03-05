""" A program to calculate the average of
    spam confidence in a given list of emails

    author: Fatih IZGI
    date: 05-Mar-2020
    version: python 3.8.1
"""

from typing import List, IO


file_name: str = input("Enter the file name: ")
values: List[float] = []  # to store the confidence values

try:  # to open the file taken by input
    path: IO = open(file_name, "r")
except FileNotFoundError:  # e.g. the user types in the wrong file name
    print(f"File not found: {file_name}")
else:
    with path:  # close path after opening
        for line in path:
            if line.startswith("X-DSPAM-Confidence:"):  # find specific lines
                try:
                    values.append(float(line[-8:-1]))  # get only the value from the line
                except ValueError:
                    print(f"Corrupted data '{line[-8:-1]}' "  # if data is corrupted
                          f"is omitted from average")  # do not include it to the average

    try:
        avg: float = sum(values) / len(values)  # calculate the average
        print(f"Average spam confidence: {round(avg, 4)}")  # round to four decimal
    except ZeroDivisionError:  # no data, empty file (len == 0) will raise ZeroDivisionError
        print("No readable data to find the average.")  # handle the error
