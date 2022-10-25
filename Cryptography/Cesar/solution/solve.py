import sys
from string import *

if len(sys.argv) != 3:
    print("[-]Usage : python3 solve.py <ENCRYPTED TEXT> <KEY>")
    sys.exit(1)

ENCRYPTED_TEXT = sys.argv[1]
KEY = sys.argv[2]
print(KEY)
n = 26
flag = ''

for i in ENCRYPTED_TEXT:
    if isalpha(i):
        if islower(i):
            shift = 65
        else:
            shift = 97

        j = (shift-(ord(i)-int(KEY))) % n + shift
        print('okay let')
print(flag)
