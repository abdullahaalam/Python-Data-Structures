fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print words[1]
    count += 1
print "There were", count, "lines in the file with From as the first word"


