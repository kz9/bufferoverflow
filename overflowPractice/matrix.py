#! /usr/bin/env python3

import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(f"Knock, knock, {sys.argv[1]}")
    else:
        sys.stderr.write(f"Usage: {sys.argv[0]} <name>")
