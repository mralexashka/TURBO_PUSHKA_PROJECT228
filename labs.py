import math


def print_matrix(matrix, width):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end='')
        print()


a = list()
n = int(input())
flag = True
a_p = list()
a_pp = list()
for i in range(n):
    a.append([int(n) for n in input().split()])
    a_p.append((i + 1) ** 2)
a_s = list()
sum_row = 0
sum_diag = 0
sum_diag2 = 0
for i in range(n):
    sum_col = 0
    sum_diag += a[i][i]
    sum_diag2 += a[n-1-i][i]
    a_s.append(sum(a[i]))
    for j in range(n):
        sum_col += a[j][i]
        if a[i][j] in a_p:
            a_pp.append(a[i][j])
    a_s.append(sum_col)
a_s.append(sum_diag2)
a_s.append(sum_diag)

for s in a_s:
    if s != sum_diag:
        flag = False
        break
for p in a_p:
    if p not in a_pp:
        flag = False
        break
print(flag)
print(a_s)
