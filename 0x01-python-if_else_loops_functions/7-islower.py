#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
      if i == ord(c):
         print("{} is lower".format(chr(c)), end="")
