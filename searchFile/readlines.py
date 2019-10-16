filename = "testdata.txt"

file =  open(filename, "r")
lines = file.readlines()

print(lines)