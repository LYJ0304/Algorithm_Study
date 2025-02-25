# 빠른 A+B
import sys

T = sys.stdin.readline()
T = int(T.rstrip())
L = []
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    L.append(A + B)

for j in L:
    print(j)





