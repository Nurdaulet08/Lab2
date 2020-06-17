n = int(input())
st = []
nd = []
rd = [[],[],[]]
for i in range(n):
	a = input().split()
	for i in range(n):
		a[i] = int(a[i])
	st.append(a)
for i in range(n):
	b = input().split()
	for i in range(n):
		b[i] = int(b[i])
	nd.append(b)

for i in range(n):
	for j in range(n):
		count = 0
		for k in range(n):
			count = nd[k][i]*st[j][k] + count
		rd[j].append(count) 

for i in range(n):
	print(*rd[i])