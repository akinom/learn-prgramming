import os

filename = "testdata.txt"

# read lines from file
file = open(filename, "r")
lines = file.readlines()

print("- print all lines")
print(lines)
print("-----------")

print("")

print("- print lines one by one")
for l in lines:
    print(l)
print("-----------")

print("")

print("- print stripped lines one by one")
for l in lines:
    print(l.strip())
print("-----------")
