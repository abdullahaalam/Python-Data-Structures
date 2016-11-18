name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        count[hour] = count.get(hour, 0) + 1
for key, value in sorted(count.items()):
    print key, value
