a = int(input())
trib = [0, 1, 1]
for i in range(a-2):
	tri = trib[i]+trib[i+1]+trib[i+2]
	trib.append(tri)
count = 0
print(trib[a])