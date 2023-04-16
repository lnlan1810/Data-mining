import numpy as np

d = 0.8

# level 0 : 1 node
# level 1 : 3 nodes
# level 2 : 7 nodes
# level 3 : 15 nodes
# .....
# level n : 2^(n+1) - 1 nodes

print("enter level of node :")
n = int(input())
m3 = (2**(n+1)) - 1
matrix = np.zeros((m3, m3), dtype=int)
matrix[0][0] = 1
for i in range(m3):
    if i * 2 + 2 <= m3:
        matrix[i][i * 2 + 1] = 1
        matrix[i][i * 2 + 2] = 1

print("matrix: ")
print(matrix)

pr = [1] * m3


def cal_pagerank(s2):
    return (1 - d) + d * s2


for a in range(10):
    for i in range(len(matrix)):
        s = 0
        col = [row[i] for row in matrix]
        for j in range(len(col)):
            if col[j] == 1:
                s += pr[j] / sum(matrix[j])

        pr[i] = cal_pagerank(s)
print("page rank: ")
print([round(num, 3) for num in pr])