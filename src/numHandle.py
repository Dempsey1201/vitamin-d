file_path = "../data/vitamin-d_afterHandle.fasta"
file_path_out = "../data/vitamin-d_FinalAfterHandle.txt"


file = open(file_path, 'r')
w = open(file_path_out, 'w')
data = read_fasta(file_path)
