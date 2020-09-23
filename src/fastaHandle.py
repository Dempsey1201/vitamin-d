import seaborn as sns
import pandas as pd

file_path = "../data/vitamin-d.fasta"
file_path_out = "../data/vitamin-d_afterHandle.fasta"


def read_fasta(filename):
    file = open(filename, 'r')
    data = {}
    for line in file:
        if line[0] == '>':
            name = line.replace('>', '').split(" ")[0]
            data[name] = ""
        else:
            data[name] += line.replace("\\n", " ").strip()
    return data


w = open(file_path_out, 'w')
data = read_fasta(file_path)
for line in data.keys():
    w.write(str(line)+'\n')
    w.write(str(data[line]) + "\n")


# print(read_fasta(file_path)['sp|P02774|VTDB_HUMAN'])
