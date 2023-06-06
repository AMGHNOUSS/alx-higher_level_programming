#!/usr/bin/python3
def uppercase(str):
    lengh = len(str)
    for i in range(0, lengh):
        ch = str[i]
        if str[i] >= 'a' and str[i] <= 'z':
            ch = ord(ch)
            ch = ch - 32
            ch = chr(ch)
        print(ch, end="")
    print("")
