
filename = "Metadata.tsv"
file = open(filename, "r")
lines = file.readlines()

print("- print lines one by one")
for l in lines:
    data = l.strip()
    print(data)
print("-----------")

