import copy

a = [[1, 2], [3, 4]]
b = a.copy()
c = list()
c = copy.deepcopy(a)
print(a)
print(c)
c[0][0] = 100
print(a)
print(c)
c[1] = 1000
print(a)
print(c)

