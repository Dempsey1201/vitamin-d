data = open("../data/1602823049.fasta", 'r')
count = 0
for line in data:
    if line[0] == '>':
        count += 1

print(count)
