#! /usr/bin/env python3
import random
import sys


def check_key(key):
    check_sum = 0
    for i in key:
        check_sum += ord(i)
    sys.stdout.write("{0:3} | {1}       \r".format(check_sum, key))
    sys.stdout.flush()
    return check_sum


if __name__ == "__main__":
    true_value = 916
    key = ""
    while True:
        key += random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEF\
                              GHIJKLMNOPQRSTUVWXYZ-_')
        s = check_key(key)
        if s == true_value:
            print(f"Found valid key: {key}")
        elif s > 916:
            key = ""
