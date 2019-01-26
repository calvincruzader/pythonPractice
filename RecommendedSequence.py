class Solution: 
	def recommendedSequence(self, s, d):
		longestWord = ''
		ptrs = [0] * len(d)
		d = list(d)


		for c in s:
			for i in range(len(ptrs)): 
				# print(ptrs[i])
				# print(d[i])
				if len(d[i]) > ptrs[i] and c == d[i][ptrs[i]]: 
					ptrs[i] += 1

					if(ptrs[i] >= len(d[i])): 
						if len(longestWord) < len(d[i]): 
							longestWord = d[i]

		return longestWord 



s = "abppplee"
d = {"able", "ale", "apple", "bale", "kangaroo"}


heyhye = Solution()
print(heyhye.recommendedSequence(s,d))
