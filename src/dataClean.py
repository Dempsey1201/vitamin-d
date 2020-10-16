w = open("../data/vitamin-d_without_unknown.txt", 'w')
data = open("../data/vitamin-d_afterHandle.fasta", 'r')
cnt = 1
for line in data:
    if cnt % 2 == 1:
        out = line
    else:
        flag = 0
        i = 0
        while i < len(line):
            if not check(line[i]):
                flag = 1
                print(str(cnt) + str(line[i]))
            i += 1
        # print(out)
        if flag == 0:
            w.write(out)
            w.write(line + '\n')
    cnt += 1
