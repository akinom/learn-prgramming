
def version0():
    names = ['arachan', 'jenny', 'monika']
    kids = [2, 1, 2]

    for i in range(len(names)):
        print(i)
        print(names[i])
        print(kids[i])
        print('---')


    for i in range(len(names)):
        print(names[i] + ' has ' + str(kids[i]) + ' children')


parentdata = [['arachan', 2], ['jenny', 1], ['monika', 10]]
print(parentdata)
ndata = len(parentdata)

for i in range(ndata):
    data = parentdata[i]
    print(data)
    # assign name to a variable
    # assign number of children to another variable
    # print as in version0():    XXXX has NNNN  children

