N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]

points = []
yet_resolved = []

for i in range(N):
    point = 0
    yet = []
    for j in range(M):
        if S[i][j] == 'o':
            point += A[j]
        else:
            yet.append(A[j])
    points.append(point + i + 1)
    yet_resolved.append(yet)

max_point = max(points)

for i in range(N):
    ans = 0
    point = points[i]
    yet = sorted(yet_resolved[i], reverse=True)
    for j in yet:
        if point < max_point:
            point += j
            ans += 1
        else:
            break
    print(ans)
