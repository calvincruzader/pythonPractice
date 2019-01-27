from collections import Counter

class Solution: 

	def numJewelsInStones(self, J, S):
		c = Counter(S)

		output = 0
		for j in J: 
			output+=c[j]
		return output

S = "aAAbbbbb"
J = "aA"

x = 0 
x = 1 if True else False 

print(x)