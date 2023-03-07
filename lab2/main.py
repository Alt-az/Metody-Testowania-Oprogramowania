#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == '.' and format_string[idx+2].isdigit():
                num = 1
                number = ''
                while format_string[idx+1+num].isdigit():
                    number+=format_string[idx+1+num]
                    num+=1
                if format_string[idx+1+num] == 'k':
                    print(param[:int(number)].swapcase(),end="")
                    shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
             if format_string[idx] == 'k':
                shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
