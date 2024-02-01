#!/usr/bin/python3


"""
prints a text with new line
"""


def text_indentation(text):
    """
    function that prints a new line after a symbol
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    # Initialise an empty string to store the formatted text
    formatted_text = ""

    new_line = [".", "?", ":"]

    # Iterate through each character in the text
    for char in text:
        # Append the current character to the formatted text
        formatted_text += char

        # If the current character is one of the new line characters, add two new lines
        if char in new_line:
            formatted_text += "\n\n"

    # Print the formatted text
    print(formatted_text.strip()) # Remove leading and trailing whitespaces
