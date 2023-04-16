import numpy as np

print("enter m (nodes) = ")
d = 0.8
m2 = int(input())
ma2 = np.zeros((m2, m2), dtype=int)
ma2[0][0] = 1
for i in range(m2):
    if i + 1 < m2:
        ma2[i][i + 1] = 1

print("matrix: ")
print(ma2)

pr = [1] * m2

def cal_pagerank(s2):
    return (1 - d) + d * s2

4
for a in range(10):
    for i in range(len(ma2)):
        s = 0
        col = [row[i] for row in ma2]
        for j in range(len(col)):
            if col[j] == 1:
                s += pr[j] / sum(ma2[j])

        pr[i] = cal_pagerank(s)


print("page rank: ")
print([round(num, 3) for num in pr])