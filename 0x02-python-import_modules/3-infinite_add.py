#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    addint = 0
    for i in range(len(argv)):
        addint += int(argv(i))
    print("{}".format(addint))
