# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on January 2021
# This program is to find the largest number

import random


def largest_number(random_list, number_of_elements):

    for loop_counter in range(0, number_of_elements):
        first = random_list[loop_counter]
        largest = first
        break

    for loop_counter in range(0, number_of_elements):
        large_number = random_list[loop_counter]
        print("The number is {0}.".format(large_number))
        if large_number > largest:
            largest = large_number
        else:
            pass

    return largest


def main():

    random_list = []
    number_of_elements = 10

    for loop_counter in range(0, number_of_elements):
        generating = random.randint(1, 100)
        random_list.append(generating)

    print("Here is a list of random numbers")
    print("")
    large = largest_number(random_list, number_of_elements)

    print("")
    print("The largest number is {0}.".format((large)))
    print("")
    print("Done!")


if __name__ == "__main__":
    main()
