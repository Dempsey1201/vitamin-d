import seaborn as sns
import pandas as pd

file_path = "../data/vitamin-d.fasta"
file_path_out = "../data/vitamin-d_afterHandle.fasta"


def check(word):
    if (word == 'G') | (word == 'A') | (word == 'V') | (word == 'L') | (word == 'I') | (word == 'P') | (word == 'F') | \
            (word == 'W') | (word == 'M') | (word == 'Y') | (word == 'S') | (word == 'T') | (word == 'C') | \
            (word == 'N') \
            | (word == 'Q') | (word == 'D') | (word == 'E') | (word == 'K') | (word == 'R') | (word == 'H') \
            | (word == '\n'):
        return True
    else:
        return False


def check_twice():
    file = open(file_path, 'r')
    for line in file:
        if line[0] != '>':
            for i in line:
                if not check(i):
                    print(i)


def read_fasta(filename):
    file = open(filename, 'r')
    data = {}
    for line in file:

        if line[0] == '>':
            name = line
            data[name] = ""
            flag = 0
        elif flag == 0:
            for i in line:
                if not check(i):
                    flag = 1
                    print(i)
                    print(name)
                    data.pop(name)
                    break
            if flag == 0:
                data[name] += line.strip()+'\n'
    return data


w = open(file_path_out, 'w')
data = read_fasta(file_path)
for line in data.keys():
    w.write(str(line))
    w.write(str(data[line]))


# print(read_fasta(file_path)['sp|P02774|VTDB_HUMAN'])
