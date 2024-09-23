import copy


def print_matrix(matrix, width):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(str(matrix[r][c]).ljust(width), end='')
        print()


a1 = list()
a2 = list()
a_m = list()
a_r = list()
n = int(input())
for _ in range(n):
    a1.append([int(k) for k in input().split()])

s = int(input())
a_m = copy.deepcopy(a1)
a_r = copy.deepcopy(a1)
for _ in range(s-1):
    for i in range(n):
        for j in range(n):
            a_r[i][j] = 0
            for p in range(n):

                a_r[i][j] += a_m[i][p] * a1[p][j]
    a_m = copy.deepcopy(a_r)

print_matrix(a_r, 3)
#gitlab check


