import numpy as np

f = [5, 15, 5, 5, 10, 10, 20, 5]
n = len(f)
L = 999999999999999999999	# Some arbitrary large number for comparison

e = [ [0] * (n + 2) for _ in range(n + 2)]
w = [ [0] * (n) for _ in range(n)]
root = [ [0] * (n) for _ in range(n)]

for i in range(n):
	w[i][i] = f[i]
	for j in range(i, n):
		w[i][j] = w[i][j - 1] + f[j]
		
for l in range(n):
	for i in range(n - l):
		j = i + l
		e[i + 1][j + 1] = L
		for k in range(i, j + 1):
			temp = e[i + 1][k] + e[k + 2][j + 1] + w[i][j]
			if temp < e[i + 1][j + 1]:
				e[i + 1][j + 1] = temp
				root[i][j] = k + 1

print("w Matrix:")
print(np.matrix(w))
print()

print("e Matrix")
print(np.matrix(e))
print()

print("Root Matrix")
print(np.matrix(root))
print()
