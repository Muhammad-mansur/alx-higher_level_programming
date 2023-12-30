#!/usr/bin/python3

def print_last_digit(number):

    # Ensure the number is non-negative
    number = abs(number)

    # Get the last digit
    last_digit = number % 10

    return last_digit
