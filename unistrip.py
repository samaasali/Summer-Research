__author__ = 'apple'

def unistrip(filename, outfile):
    data = open(filename, "r")
    header = data.readline()

    new = open(outfile, "w")

    new.write(header)

    for line in data:
        mylist = line.split()

        if "UNIVERSITY" in mylist:
            new.write(" ". join(mylist) + "\n")

