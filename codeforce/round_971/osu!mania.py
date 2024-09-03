# solving beatmap solver
t = int(input())
for i in range(t):
    nl = int(input())
    res = []
    for j in range(nl):
        res.append(list(input()).index('#') + 1)
    print(*res[::-1])