from sage.all import *

def immutabilize(m):
	M = copy(m)
	M.set_immutable()
	return M

n = 4

S = {
		# immutabilize(matrix([(0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)])),
		# immutabilize(matrix([(0, 0, 0, 1), (1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 1), (0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 1), (1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 1), (0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 0, 1, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(1, 0, 1, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0)])),
		# immutabilize(matrix([(0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 1, 0, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 1, 1, 0), (0, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 1, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 0, 0), (0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 0, 0), (1, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 1)])),
		# immutabilize(matrix([(0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)])),
		# immutabilize(matrix([(0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 1), (1, 0, 0, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 1, 0, 1), (0, 0, 1, 1), (0, 0, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 0, 1), (0, 0, 1, 1), (1, 0, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 1, 0, 0), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(1, 1, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 0), (1, 0, 0, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (1, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 1, 0, 0), (0, 0, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 0), (0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 1, 0, 0), (0, 0, 1, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 1, 0, 0), (0, 1, 0, 0), (0, 0, 1, 1)])),
		immutabilize(matrix([(1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 1)])),
		immutabilize(matrix([(1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (0, 1, 1, 1), (0, 0, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 0, 1, 0), (1, 0, 1, 0), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 0, 0, 1), (0, 1, 1, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 1), (1, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 1), (1, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0), (1, 1, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 1, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 1, 1, 0), (0, 0, 0, 1), (1, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 1, 0, 0), (1, 0, 0, 0), (1, 0, 1, 0)])),
		immutabilize(matrix([(1, 1, 0, 0), (0, 0, 0, 1), (1, 0, 0, 0), (1, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 1, 0, 0), (0, 0, 0, 1), (1, 0, 1, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1), (1, 1, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0), (1, 1, 1, 0)])),
		immutabilize(matrix([(1, 0, 1, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 1, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 1, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 1, 1, 0), (1, 0, 0, 1), (0, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 1, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 1, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 1, 0, 1), (1, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 0, 1, 0), (1, 0, 0, 0), (1, 1, 0, 1)])),
		immutabilize(matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 0), (1, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 0, 0, 0), (0, 1, 0, 0), (1, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 1, 1, 0), (1, 0, 1, 1), (0, 0, 0, 1), (0, 0, 1, 0)])),
		immutabilize(matrix([(1, 1, 1, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 1, 1)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 0, 1, 1), (1, 1, 1, 0), (0, 0, 1, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 1, 1)])),
		immutabilize(matrix([(0, 1, 1, 1), (0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0)])),
		immutabilize(matrix([(0, 1, 1, 1), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1)])),
		immutabilize(matrix([(0, 1, 0, 1), (1, 1, 1, 1), (1, 1, 1, 0), (0, 1, 1, 1)])),
		immutabilize(matrix([(0, 1, 0, 1), (1, 1, 1, 1), (0, 1, 1, 1), (1, 1, 1, 0)])),
		immutabilize(matrix([(1, 0, 1, 1), (0, 1, 0, 0), (1, 1, 0, 1), (1, 0, 0, 0)])),
		immutabilize(matrix([(1, 0, 1, 1), (0, 1, 0, 0), (1, 0, 0, 0), (1, 1, 0, 1)])),
		immutabilize(matrix([(1, 1, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (1, 1, 1, 1)])),
		immutabilize(matrix([(1, 1, 1, 0), (0, 0, 1, 1), (1, 1, 1, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 1, 1), (1, 1, 1, 0), (0, 1, 0, 0), (1, 1, 1, 1)])),
		immutabilize(matrix([(0, 0, 1, 1), (1, 1, 1, 0), (1, 1, 1, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 1, 1, 1), (0, 1, 0, 0), (1, 1, 0, 1)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 1, 1, 1), (1, 1, 0, 1), (0, 1, 0, 0)])),
		immutabilize(matrix([(0, 1, 0, 1), (0, 0, 0, 1), (1, 1, 0, 1), (1, 0, 1, 1)])),
		immutabilize(matrix([(0, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1), (1, 0, 1, 1)])),
		immutabilize(matrix([(0, 0, 0, 1), (1, 1, 1, 1), (0, 1, 0, 1), (1, 0, 0, 1)])),
		immutabilize(matrix([(1, 1, 1, 1), (0, 0, 0, 1), (0, 1, 0, 1), (1, 0, 0, 1)])),
}


P = sage.combinat.permutation.Permutations(n)
P = { immutabilize(p.to_matrix()) for p in P }
# fullyTested = set()
P.remove(immutabilize(copy(matrix.identity(n))))
# print(P)
# print()
sizeT = len(P)
flag = True
ctr = 0
while flag:
	if(immutabilize(copy(matrix.identity(n))) in P):
		flag = False
		break
	ctr += 1
	print("iteration: " + str(ctr), "   size: " + str(len(P)))
	flag = False
	orig = P
	for s in range(n):
		for t in range(s+1,n):
			# TOP ROW 0s
			A = copy(matrix.identity(n))
			A[t,s] = 1
			A_p = copy(A)
			A_p[s,s] = 0
			A_p[s,t] = 1
			
			# AP = {immutabilize(A*p % 2) for p in P.difference(fullyTested)}
			# A_pP = {immutabilize(A_p*p % 2) for p in P.difference(fullyTested)}
			AP = {immutabilize(A*p % 2) for p in P}
			A_pP = {immutabilize(A_p*p % 2) for p in P}
			
			P = P.union(AP.intersection(A_pP))
			

			T = set()
			for m in S:
				if(m in AP.intersection(A_pP)):
					# print(str(s) + " " + str(t) + " TOP:")
					print("matrix(" + str(list(m)) + ") # (" + str(s) + "," + str(t) + ",0),")
					# print("--")
					T.add(m)
			S = S.difference(T)
			if (len(S) == 0):
				exit()
			
			if len(P) > sizeT:
				flag = True
				sizeT = len(P)
			


			# BOT ROW 0s
			A = copy(matrix.identity(n))
			A[s,t] = 1
			A_p = copy(A)
			A_p[t,t] = 0
			A_p[t,s] = 1
			
			# AP = {immutabilize(A*p % 2) for p in P.difference(fullyTested)}
			# A_pP = {immutabilize(A_p*p % 2) for p in P.difference(fullyTested)}
			AP = {immutabilize(A*p % 2) for p in P}
			A_pP = {immutabilize(A_p*p % 2) for p in P}

			P = P.union(AP.intersection(A_pP))
			

			T = set()
			for m in S:
				if(m in AP.intersection(A_pP)):
					# print(str(s) + " " + str(t) + " BOT:")
					print("matrix(" + str(list(m)) + ") # (" +  str(s) + "," + str(t) + ",1),")
					# print("--")
					T.add(m)
			S = S.difference(T)
			if (len(S) == 0):
				exit()

			
			if len(P) > sizeT:
				flag = True
				sizeT = len(P)
	# fullyTested = orig

# for p in P:
# 	print(p)
# 	print("--")
if(immutabilize(copy(matrix.identity(n))) in P):	
	print("n = " + str(n) + ": Uh oh!")
else:
	print("n = " + str(n) + ": All good!")