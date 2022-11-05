import os
import sys

def readInt(prefix,error = 'Invalid number',_range=None,breakOnError = False):
    while True:
        try:
            num = int(input(prefix + ': '))
            if _range is None:
                return num
            if _range[0] <= num <= _range[1]:
                return num
            print('Invalid range(', _range[0], ',', _range[1], ')')
        except:
            if breakOnError:
                return None
            print(error)

def isWindows():
    return sys.platform in ['win32','win64','windows']

def clear():
    if isWindows():
        os.system('cls')
    else:
        os.system('clear')
