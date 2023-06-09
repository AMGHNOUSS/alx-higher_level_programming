#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lengh = len(sys.argv) - 1
    if lengh == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(lengh))
        for i in range(1, lengh + 1):
            print("{}: {}".format(i, sys.argv[i]))
