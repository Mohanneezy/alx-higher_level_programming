#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            i =ord(c) -32
            print("{}".format(chr(i)), end="")
