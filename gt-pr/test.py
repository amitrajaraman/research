from sage.all import *

n = 4

Id = copy(matrix.identity(n))
s = 0
t = 3
A = copy(matrix.identity(n))
A[t,s] = 1
A_p = copy(A)
A_p[s,s] = 0
A_p[s,t] = 1

print((A**(-1)*Id) % 2)
print("--")
print((A_p**(-1) * Id) % 2)
print("--")

## FOR n = 4
## Id goes to T in (0,3)