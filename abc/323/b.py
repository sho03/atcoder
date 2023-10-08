N = int(input())
S = [input() for _ in range(N)]



d = dict()
for i in range(N):
    d[i] = S[i].count('o')

sorted_d = sorted(d.items(), key=lambda x:(-x[1], x[0]))

ans = [item[0] + 1 for item in sorted_d]
print(' '.join(map(str, ans)))
