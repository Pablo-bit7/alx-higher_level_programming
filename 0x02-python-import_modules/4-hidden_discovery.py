#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfunctions = dir()
    for i in range(0, len(allfunctions)):
        print("{:s}".format(allfunctions[i]))
