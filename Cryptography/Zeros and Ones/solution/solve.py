import sys

if (len(sys.argv) != 2):
    print("[-]Usage: python3 solve.py <BINARY ENCODING")
    sys.exit()


flag = ''
ENCODED_BINARY = sys.argv[1].split(' ')
for i in ENCODED_BINARY:
    flag += chr(int('0b'+i, 0))
print(flag)
