class Node: 
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right 


	def serialize(root):



	def deserialize(s): 


	
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

