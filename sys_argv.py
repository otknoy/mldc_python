import sys

names = sys.argv[1:]

for name in names:
    f = open(name)
    print f.read()
    f.close()

# f = open(sys.argv[1])

# print f.read()

# f.close()
