import sys
input = sys.stdin.readline


def trans(son, parent):
    while True:
        if son in tree:
            if tree[son] == parent:
                return 1
            else:
                son = tree[son]
        else:
            return 0


N = int(input())
tree = dict()
for _ in range(N - 1):
    S, P = input().split()
    tree[S] = P

A, B = input().split()
print(trans(A, B) or trans(B, A))