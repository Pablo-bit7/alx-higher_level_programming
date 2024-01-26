#!/usr/bin/env python3
def uppercase(str):
    for char in str:
        upper_char = char
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        print("{:s}".format(upper_char), end="")
    print()  # Print a newline after processing the string
