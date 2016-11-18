name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    word = line.split()
    if line.startswith('From '):
        count[word[1]] = count.get(word[1], 0) + 1

largest = 0
email = ''
for key in count:
    if  count[key] > largest:
        largest = count[key]
        email = key
print email, largest
