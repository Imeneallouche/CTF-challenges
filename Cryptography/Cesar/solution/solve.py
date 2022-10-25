import sys
from string import *

if len(sys.argv) != 3:
    print("[-]Usage : python3 solve.py <ENCRYPTED TEXT> <KEY>")
    sys.exit(1)

ENCRYPTED_TEXT = sys.argv[1]
KEY = sys.argv[2]

n = 26
flag = ''

for i in ENCRYPTED_TEXT:
    if i.isalpha():
        if i.islower():
            shift = 97
        else:
            shift = 65

        j = ord(i)-int(KEY)-shift
        flag += chr(j % n + shift)
    else:
        flag += i

print(flag)
