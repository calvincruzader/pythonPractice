class Solution: 

	def reverseWords(self, words): 
		return " ".join(list(reversed(list(words.split(" ")))))


s = Solution()
print(s.reverseWords("test hey there"))