#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 20, 2023
# This program gets a number from the user from 1-12 and will tell them what month it represents.

# get the user number representing a month
month = input("Please enter a number from 1-12 (Starting with January = 1): ")

# check and display the month to the suers number
match month:
    case "1":
        print("{} represents January.".format(month))

    case "2":
        print("{} represents February.".format(month))

    case "3":
        print("{} represents March.".format(month))

    case "4":
        print("{} represents April.".format(month))

    case "5":
        print("{} represents May.".format(month))

    case "6":
        print("{} represents June.".format(month))

    case "7":
        print("{} represents July.".format(month))

    case "8":
        print("{} represents August.".format(month))

    case "9":
        print("{} represents September.".format(month))

    case "10":
        print("{} represents October.".format(month))

    case "11":
        print("{} represents November.".format(month))

    case "12":
        print("{} represents December.".format(month))

    case _:
        print("{} does not represent a month.".format(month))
