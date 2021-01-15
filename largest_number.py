# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to find the largest number

import random


def largest_number(random_list):
    # this function calculates the largest number

    number_of_elements = len(random_list)
    largest = random_list[0]

    for loop_counter in range(0, number_of_elements):
        large_number = random_list[loop_counter]
        if large_number > largest:
            largest = large_number

    return largest


def main():

    random_list = []
    number_of_elements = 10
    print("Here is a list of random numbers")
    print("")
    for loop_counter in range(0, number_of_elements):
        generating = random.randint(1, 100)
        print("The number is {0}.".format(generating))
        random_list.append(generating)

    print("")
    large = largest_number(random_list)

    print("")
    print("The largest number is {0}.".format((large)))
    print("")
    print("Done!")


if __name__ == "__main__":
    main()
