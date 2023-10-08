from itertools import product
from itertools import combinations 

# 入力
# 一つの数字(3)
n = int(input())

# 複数の数字(3 4)
n, m = map(int, input().split())

# 文字列("hoge")
s = input()

# 複数の文字列("hoge" "huga")
s1, s2 = input().split()

# リストとして受け取る(以下は数値のリスト)
l = list(map(int, input().split()))

# 文字列リスト
l = list(input().split())

# bit全探索で使うと良さげなもの
# 下記の場合、各要素が0 or 1で要素数が5のタプルが(2 ** 5)分生成される
p = product((0, 1), repeat=5)
# (0, 0, 0, 0, 0)
# (1, 0, 0, 0, 0)
# (1, 1, 0, 0, 0)
# ....
# (1, 1, 1, 1, 1)

# 組み合わせ
# 下記の場合、[abcde]から3文字を選ぶ組み合わせをタプルで生成する
c = list(combinations("abcde", 3))
# (a, b, c)
# (a, b, d)
# ...
# (c, d, e)


# 累積和
def ruisekiwa(l):
    ruisekiwa = [0 for i in range(len(l))]
    for i in range(1, len(ruisekiwa)):
        ruisekiwa[i] = ruisekiwa[i - 1] + l[i - 1]