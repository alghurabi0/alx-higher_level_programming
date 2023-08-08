#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 1:
        print("{:c}".format(i - 32), end="")
    else:
        print("{:c}".format(i), end="")
