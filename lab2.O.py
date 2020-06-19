def f(l, r, a):
    mx = 0
    ans = 0
    for i in range(l, r + 1):
        if a[i] > mx:
            ans += 1
            mx = a[i]
    return ans

n = int(input())
a = list(map(int, input().split()))

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(f(l, r, a))