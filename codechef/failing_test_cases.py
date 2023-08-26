def codechef_code(n,m):
	mod = 10**9 + 7
	maxn = 2 * 10**6 + 10
	fac = [i for i in range(maxn)]
	fac[0] = 1
	for i in range(1, maxn):
		fac[i] *= fac[i-1]
		fac[i] %= mod

	ifac = [0]*maxn
	ifac[-1] = pow(fac[-1], mod-2, mod)
	for i in reversed(range(maxn-1)):
		ifac[i] = (i+1) * ifac[i+1] % mod

	def C(n, r):
		if n < r or r < 0: return 0
		return fac[n] * ifac[r] * ifac[n-r]  % mod

	if m == 0:
		return 1
	if m == 1:
		return n+1

	ans = 1
	for i in range(m+1): ans += C(n-1, i)
	ans %= mod
	val = 1
	for i in range(2, n+1):
		# i is the first position where it goes bad
		# 2^(n-i) * sum(C(i-2, k) for k <= m-2)
		ans += val * pow(2, n-i, mod)
		ans %= mod
		
		val *= 2
		val -= C(i-2, m-2)
		val %= mod
	return ans


def my_code(n,m):
	mod = 10**9 + 7

	def fact(n):
		res = 1
		for i in range(1,n+1):
			res = (res*i) % mod
		return res

	# def CC(X,i,j):
	#     res = X/j
	#     for k in range(1,j):
	#         # print("CC(n,r) multiplying",X-k,i-X-1-k,"dividing",j-k,j-k)
	#         res = ((res*(X-k)*((i-X-1)-k))/((j-k)*(j-k)))%mod
	#     return res

	def C(n,r):
		return fact(n) * pow(fact(r),-1,mod) * pow(fact(n-r),-1,mod)

	def no_of_seq(n):
		if n==1:
			return 1
		elif n==2:
			return 3
		else:
			X = 1 # for n=3
			p = 1
			for _ in range(4,n+1):
				p = (p*2) % mod
				X = (X*2 + p) % mod
			p = (p * 2) % mod
			return ((3*p) % mod + (2*X) % mod) % mod


	def no_of_bad_seq(n,m):
		result = 0
		if m+1==n:
			result += 1
		elif m<n:
			result = pow(2,n-m-1,mod)
			# print("at index i=",m," subtract ",result)
			p = result
			for i in range(m+1,n):
				# for m-1 in i-1
				res_m = 0
				if m==1:
					res_m = 1
				else:
					j = 1
					for j in range(1,min(m,i-m)+1):
					# while (j<=m and j<=i-m):
						res_m = (res_m + (C(m,j) * C(i-m-1,j-1))%mod)% mod
						# res_m = (res_m + CC(m,i,j))% mod
						# j += 1

				# for m in i-1
				res_m_plus_1 = 0
				if i==m+1:
					res_m_plus_1=1
				else:
					j = 1
					for j in range(1,min((m+1),i-(m+1))+1):
					# while (j<=(m+1) and j<=i-(m+1)):
						res_m_plus_1 = (res_m_plus_1 + C(m+1,j) * C(i-(m+1)-1,j-1)) % mod
						# res_m_plus_1 = (res_m_plus_1 + CC(m+1,i,j)) % mod
						# j += 1
				p = p*pow(2,-1,mod)
				result = (result + (p*((res_m + res_m_plus_1)%mod))%mod + (no_of_seq(n-i)*res_m_plus_1)%mod) % mod
				# print("at index i=",i," subtract ",result, " # ", pow(2,n-i-1,mod)," ",res_m," ",res_m_plus_1," ",no_of_seq(n-i))
		return int(result)

	if m == 0:
		return 1
	else:
		# print("total: ", no_of_seq(n))
		result = (no_of_seq(n) - no_of_bad_seq(n,m) + 1) % mod
		if result<0:
			result += mod
		return int(result)


import unittest
import time

class TestCase(unittest.TestCase):
	def testcase1(self):

		for i in range(100, 1000):
			for j in range(int(i/2),i+3):
				print("n , m = ",i,j)
				t1 = time.time()
				my_code1 = my_code(i,j)
				print("my code time:",time.time() - t1)
				# print("my code: ", my_code1)
				t1 = time.time()
				codechef_code1 = codechef_code(i,j)
				print("codechef code time:",time.time() - t1)
				# print("codechef code: ", codechef_code1)
				self.assertEqual(my_code1, codechef_code1)

unittest.main()


# testing results
# till 12 1 everything matches.
