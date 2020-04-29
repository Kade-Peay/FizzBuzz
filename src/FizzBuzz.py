#!/bin/env python3
import sys

def FizzBuzz():
    for i in range(100):
        output = ""

        if(i % 3 == 0): output += "FIZZ"
        if(i % 5 == 0): output += "BUZZ"
        elif(i % 3 != 0) and (i % 5 != 0): output += str(i)
        print(output)

def FuzzBizz():
    for i in range(100):
        output = ""

        if(i % 7 == 0): output += "FIZZ"
        if(i % 9 == 0): output += "BUZZ"
        elif(i % 7 != 0) and (i % 9 != 0): output += str(i)
        print(output)


if __name__ == "__main__":

    options = ['FizzBuzz', 'FuzzBizz']

    if len(sys.argv) < 2:
        print("Please speicfy either FizzBuzz or FuzzBizz")
    elif sys.argv[1] not in options:
        print("Pick either FizzBuzz or FuzzBizz")
    elif sys.argv[1] == 'FizzBuzz':
        FizzBuzz()
    elif sys.argv[1] == 'FuzzBizz':
        FuzzBizz()  