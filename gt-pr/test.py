from sage.all import *

def retA(s,t,bot):
	A = copy(matrix.identity(n))
	if(bot == 0):
		A[t,s] = 1
	else:
		A[s,t] = 1
	A_p = copy(A)
	if(bot == 0):
		A_p[s,s] = 0
		A_p[s,t] = 1
	else:
		A_p[t,t] = 0
		A_p[t,s] = 1
	return A, A_p			

n = 4

# S = [
# 		copy(matrix.identity(n)) # 0 3 TOP
# 	]

# S = [
# 		matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,0,0,1]]), # 0 2 BOT
# 		matrix([[1,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,0]]) # 1 2 BOT
# 	]

# S = [
# 		matrix([[1,0,1,0],[0,1,0,0],[0,0,1,0],[1,0,0,1]]), # 0 1 BOT
# 		matrix([[0,0,1,0],[0,1,0,0],[1,0,1,0],[1,0,0,1]]), # 1 2 BOT
# 		matrix([[1,0,0,1],[0,1,1,0],[0,0,1,0],[1,0,0,0]]), # 0 2 BOT
# 		matrix([[1,0,0,1],[0,0,1,0],[0,1,1,0],[1,0,0,0]]) # 0 1 BOT
# 	]
# st = [(0,1,1), (1,2,1), (0,2,1), (0,1,1)]

# S = [
# 		matrix([(1, 1, 1, 0), (0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 1)]), # 2 3 BOT
# 		matrix([(0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 1, 0), (1, 0, 0, 1)]), # 1 3 BOT
# 		matrix([(0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 1, 0), (1, 0, 0, 1)]), # 2 3 BOT
# 		matrix([(0, 0, 1, 0), (1, 0, 1, 0), (1, 1, 1, 0), (1, 0, 0, 1)]), # 2 3 BOT
# 		matrix([(1, 0, 1, 1), (0, 1, 1, 0), (0, 0, 1, 0), (1, 0, 0, 0)]), # 0 1 BOT
# 		matrix([(0, 0, 1, 0), (0, 1, 1, 0), (1, 0, 1, 1), (1, 0, 0, 0)]), # 0 1 TOP
# 		matrix([(1, 0, 1, 1), (0, 0, 1, 0), (0, 1, 1, 0), (1, 0, 0, 0)]), # 2 3 BOT
# 		matrix([(0, 0, 1, 0), (1, 0, 1, 1), (0, 1, 1, 0), (1, 0, 0, 0)])  # 1 3 BOT
# 	]
# st = [(2,3,1), (1,3,1), (2,3,1), (2,3,1), (0,1,1), (0,1,0), (2,3,1), (1,3,1)]

# S = [
# 		matrix([(1, 1, 1, 0), (0, 1, 0, 0), (1, 0, 1, 1), (1, 0, 0, 1)]), # 1 2 BOT
# 		matrix([(1, 1, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1), (1, 0, 1, 1)]), # 1 2 TOP
# 		matrix([(0, 1, 0, 0), (0, 1, 1, 1), (0, 0, 1, 0), (1, 0, 0, 1)]), # 0 2 TOP
# 		matrix([(0, 1, 0, 0), (1, 0, 0, 1), (0, 0, 1, 0), (0, 1, 1, 1)]), # 0 3 TOP
# 		matrix([(0, 0, 1, 0), (1, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)]), # 1 3 TOP
# 		matrix([(0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 0, 1), (0, 0, 1, 1)]), # 1 2 BOT
# 		matrix([(0, 0, 1, 0), (1, 0, 1, 0), (0, 1, 1, 1), (1, 0, 0, 1)]), # 1 3 TOP
# 		matrix([(0, 0, 1, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 1)]), # 1 3 TOP
# 		matrix([(1, 1, 0, 1), (0, 1, 1, 0), (0, 0, 1, 0), (1, 0, 0, 0)]), # 2 3 BOT
# 		matrix([(0, 1, 1, 0), (1, 1, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0)]), # 1 3 BOT
# 		matrix([(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 1, 1), (1, 0, 0, 0)]), # 2 3 BOT
# 		matrix([(0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 1, 1), (1, 0, 0, 0)]), # 2 3 BOT
# 		matrix([(1, 0, 1, 1), (0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 0, 0)]), # 1 3 TOP
# 		matrix([(1, 0, 1, 1), (0, 0, 1, 0), (1, 0, 0, 0), (1, 1, 1, 0)]), # 1 3 TOP
# 		matrix([(0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 1, 0), (1, 0, 0, 0)]), # 0 1 TOP
# 		matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1)]), # 0 2 TOP
# 	]
# st = [(1,2,1), (1,2,0), (0,2,0), (0,3,0), (1,3,0), (1,2,1), (1,3,0), (1,3,0), (2,3,1), (1,3,1), (2,3,1), (2,3,1), (1,3,0), (1,3,0), (0,1,0), (0,2,0)]

# S = [
# 		matrix([(0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 1), (1, 0, 0, 0)]), # (0,2,0),
# 		matrix([(0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 0, 0)]), # (0,2,0),
# 		matrix([(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 1)]), # (0,3,0),
# 		matrix([(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 1, 1), (1, 0, 0, 0)]), # (1,2,0),
# 		matrix([(0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 1, 1)]), # (1,3,0),
# 		matrix([(0, 1, 0, 0), (1, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1)]), # (2,3,0),
# 		matrix([(0, 1, 1, 0), (0, 1, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0)]), # (0,1,0),
# 		matrix([(0, 0, 1, 1), (1, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0)]), # (0,1,0),
# 		matrix([(0, 0, 1, 0), (1, 1, 1, 0), (0, 0, 1, 1), (0, 1, 1, 1)]), # (0,1,0),
# 		matrix([(0, 0, 1, 0), (1, 0, 1, 0), (1, 0, 0, 1), (1, 1, 0, 1)]), # (0,1,0),
# 		matrix([(0, 0, 1, 0), (1, 0, 1, 0), (0, 1, 1, 1), (0, 0, 1, 1)]), # (0,1,0),
# 		matrix([(1, 0, 1, 1), (0, 0, 1, 0), (1, 0, 0, 0), (1, 1, 0, 0)]), # (0,1,1),
# 		matrix([(0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 1, 1), (1, 0, 1, 0)]), # (0,2,0),
# 		matrix([(0, 1, 1, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 1)]), # (0,2,1),
# 		matrix([(0, 0, 1, 0), (0, 1, 1, 1), (1, 0, 0, 1), (0, 0, 1, 1)]), # (0,3,0),
# 		matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 1), (0, 0, 1, 1)]), # (0,3,0),
# 		matrix([(1, 0, 1, 1), (0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 1, 0)]), # (0,3,1),
# 		matrix([(1, 0, 1, 1), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0)]), # (0,3,1),
# 		matrix([(1, 0, 1, 1), (1, 0, 1, 0), (1, 1, 1, 0), (0, 0, 1, 0)]), # (1,2,0),
# 		matrix([(1, 1, 0, 1), (0, 1, 1, 0), (1, 0, 1, 0), (1, 0, 0, 0)]), # (1,2,1),
# 		matrix([(0, 1, 0, 0), (0, 1, 1, 1), (0, 1, 1, 0), (1, 0, 0, 1)]), # (1,2,1),
# 		matrix([(0, 0, 1, 0), (1, 1, 0, 1), (1, 0, 0, 1), (1, 0, 1, 0)]), # (1,2,1),
# 		matrix([(0, 0, 1, 0), (0, 1, 1, 1), (0, 0, 1, 1), (1, 1, 1, 0)]), # (1,2,1),
# 		matrix([(1, 1, 0, 1), (0, 1, 1, 0), (1, 0, 0, 0), (1, 0, 1, 0)]), # (1,3,1),
# 		matrix([(1, 1, 1, 0), (1, 1, 0, 1), (0, 1, 0, 0), (1, 0, 1, 1)]), # (0,1,0),
# 		matrix([(0, 1, 1, 0), (0, 1, 1, 1), (0, 1, 0, 0), (1, 0, 0, 1)]), # (0,1,1),
# 		matrix([(1, 1, 1, 0), (1, 1, 1, 1), (1, 0, 1, 1), (1, 0, 0, 1)]), # (0,2,0),
# 		matrix([(1, 1, 1, 0), (1, 0, 1, 1), (1, 1, 1, 1), (1, 0, 0, 1)]), # (0,2,0),
# 		matrix([(1, 1, 1, 0), (0, 1, 0, 0), (1, 1, 0, 1), (1, 0, 1, 1)]), # (0,3,1),
# 		# matrix([(0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 1, 0), (1, 0, 0, 0)]),
# 		# matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 1)]),
# 		# matrix([(0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 0, 1, 1)]),
# 	]
# st = [(0,2,0),(0,2,0),(0,3,0),(1,2,0),(1,3,0),(2,3,0)] + [(0,1,0)]*5 + [(0,1,1),(0,2,0),(0,2,1),(0,3,0),(0,3,0),(0,3,1),(0,3,1),(1,2,0)] + [(1,2,1)]*4 + [(1,3,1),(0,1,0),(0,1,1),(0,2,0),(0,2,0),(0,3,1)]

S = [
		# matrix([(0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1), (1, 0, 0, 0)]),
		# matrix([(0, 0, 0, 1), (0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0)]),
		# matrix([(0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0)]),
		# matrix([(0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0)]),
		# matrix([(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 0, 1)]),
		# matrix([(0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0)]),
		# matrix([(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 0, 0, 0)]),
		# matrix([(0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0)]),
		# matrix([(0, 1, 0, 0), (0, 0, 1, 0), (1, 0, 0, 0), (0, 0, 0, 1)]),
		# matrix([(0, 1, 0, 0), (0, 0, 0, 1), (1, 0, 0, 0), (0, 0, 1, 0)]),
		matrix([(0, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 1)]), # (0,3,0),
		matrix([(0, 0, 1, 1), (0, 1, 1, 0), (0, 0, 1, 0), (1, 0, 0, 0)]), # (1,2,1),
		matrix([(0, 0, 1, 1), (1, 0, 1, 0), (0, 0, 1, 0), (0, 1, 0, 0)]), # (1,2,1),
		matrix([(1, 0, 0, 1), (1, 1, 0, 0), (1, 0, 0, 0), (0, 0, 1, 0)]), # (1,2,1),
		matrix([(1, 0, 1, 0), (0, 0, 1, 1), (0, 0, 1, 0), (0, 1, 0, 0)]), # (1,2,1),
		matrix([(0, 1, 0, 0), (1, 0, 0, 1), (0, 0, 0, 1), (0, 0, 1, 0)]), # (1,2,1),
		matrix([(0, 1, 1, 0), (0, 0, 1, 1), (0, 0, 1, 0), (1, 0, 0, 0)]), # (1,2,1),
		matrix([(0, 1, 0, 0), (0, 0, 0, 1), (0, 1, 1, 0), (1, 0, 0, 1)]), # (1,3,0),
		matrix([(0, 1, 0, 0), (1, 0, 0, 1), (0, 0, 1, 0), (0, 0, 0, 1)]), # (1,3,1),
		matrix([(1, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0), (1, 1, 0, 0)]), # (2,3,0),
		matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 0, 1)]), # (2,3,0),
		matrix([(0, 0, 1, 0), (1, 0, 0, 1), (1, 0, 0, 0), (1, 1, 0, 0)]), # (2,3,0),
		matrix([(0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 0, 1), (1, 0, 0, 1)]), # (2,3,0),
		matrix([(0, 1, 0, 1), (0, 0, 1, 1), (0, 0, 1, 0), (1, 0, 1, 0)]), # (2,3,0),
		matrix([(1, 1, 0, 0), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 1, 1)]), # (2,3,0),
		matrix([(0, 0, 1, 0), (1, 0, 0, 0), (1, 0, 0, 1), (1, 1, 0, 1)]), # (2,3,0),
		matrix([(0, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 0), (1, 0, 0, 1)]), # (2,3,0),
		matrix([(1, 0, 0, 0), (0, 0, 1, 0), (1, 0, 0, 1), (1, 1, 0, 1)]), # (2,3,0),
		matrix([(0, 0, 1, 0), (1, 1, 0, 0), (0, 0, 1, 1), (0, 1, 1, 1)]), # (2,3,0),
		matrix([(1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 1, 1), (0, 0, 1, 1)]), # (2,3,1),
		matrix([(0, 0, 1, 0), (0, 1, 1, 1), (1, 0, 0, 1), (0, 0, 0, 1)]), # (2,3,1),
		matrix([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 1, 1), (0, 0, 1, 1)]), # (2,3,1),
		matrix([(0, 0, 0, 1), (0, 0, 1, 0), (1, 1, 1, 0), (1, 0, 1, 0)]), # (2,3,1),
		matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 1), (0, 0, 0, 1)]), # (2,3,1),
		matrix([(0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 1), (1, 0, 1, 0)]), # (0,1,0),
		matrix([(0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (1, 1, 1, 0)]), # (0,1,0),
		matrix([(0, 0, 0, 1), (0, 1, 1, 1), (1, 0, 0, 1), (0, 0, 1, 0)]), # (0,1,0),
		matrix([(1, 1, 0, 1), (1, 1, 0, 0), (1, 0, 0, 0), (1, 0, 1, 0)]), # (0,1,1),
		matrix([(1, 0, 1, 1), (1, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 0)]), # (0,1,1),
		matrix([(1, 1, 0, 1), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 0)]), # (0,1,1),
		matrix([(0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 1, 1), (1, 1, 1, 0)]), # (0,2,0),
		matrix([(1, 0, 1, 0), (0, 0, 1, 0), (1, 1, 1, 0), (0, 0, 0, 1)]), # (0,2,0),
		matrix([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 1, 1), (0, 0, 1, 0)]), # (0,2,0),
		matrix([(1, 1, 0, 1), (1, 0, 1, 0), (1, 1, 0, 0), (1, 0, 0, 0)]), # (0,2,1),
		matrix([(1, 0, 1, 1), (0, 1, 0, 0), (1, 0, 1, 0), (0, 0, 1, 0)]), # (0,2,1),
		matrix([(1, 1, 0, 1), (1, 0, 1, 0), (1, 0, 0, 0), (1, 1, 0, 0)]), # (0,3,0),
		matrix([(0, 0, 1, 0), (1, 0, 0, 1), (0, 1, 0, 0), (1, 0, 1, 0)]), # (0,3,0),
		matrix([(0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0)]), # (0,3,0),
		matrix([(1, 1, 1, 0), (1, 0, 1, 1), (0, 0, 0, 1), (1, 0, 0, 1)]), # (1,3,0),
		matrix([(0, 0, 0, 1), (1, 0, 1, 1), (1, 1, 1, 0), (1, 0, 0, 1)]), # (1,3,0),
		matrix([(0, 1, 1, 1), (0, 0, 0, 1), (0, 1, 0, 0), (1, 0, 0, 1)]), # (1,3,0),
		matrix([(0, 1, 0, 1), (1, 1, 1, 1), (1, 1, 1, 0), (1, 0, 0, 1)]), # (2,3,0),
		matrix([(1, 0, 1, 1), (0, 1, 0, 0), (1, 1, 0, 1), (0, 1, 0, 1)]), # (2,3,0),
		matrix([(1, 1, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (1, 0, 1, 1)]), # (2,3,0),
		matrix([(0, 0, 1, 1), (1, 1, 1, 0), (0, 1, 0, 0), (1, 0, 1, 1)]), # (2,3,0),
		matrix([(0, 0, 0, 1), (0, 1, 1, 1), (0, 1, 0, 0), (1, 0, 0, 1)]), # (2,3,0),
		matrix([(0, 1, 0, 1), (0, 1, 0, 0), (1, 1, 0, 1), (1, 0, 1, 1)]), # (0,1,0),
		matrix([(1, 1, 1, 0), (1, 1, 1, 1), (0, 1, 0, 1), (1, 0, 0, 1)]), # (0,1,1),
	]

st = [(0,3,0)] + [(1,2,1)]*6 + [(1,3,0),(1,3,1)] + [(2,3,0)]*10 + [(2,3,1)]*5 + [(0,1,0)]*3 + [(0,1,1)]*3 + [(0,2,0)]*3 + [(0,2,1)]*2 + [(0,3,0)]*3
st = st + [(1,3,0)]*3 + [(2,3,0)]*5 + [(0,1,0),(0,1,1)]

# S = [
		
# 	]

retList = []

for i in range(len(S)):
	# print(str(i) + "/" + str(len(S)))
	A, A_p = retA(*st[i])
	retList.append(list((A**(-1) * S[i]) % 2))
	retList.append(list((A_p**(-1) * S[i]) % 2))
	
for elem in retList:
	print("immutabilize(matrix(" + str(elem) + ")),")
	# print("matrix(" + str(elem) + "),")
# print(retList)

## FOR n = 4
## Id goes to T in (0,3)