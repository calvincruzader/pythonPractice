from collections import deque

class MathNode: 
  def __init__(self, val):
    self.val, self.mult_node, self.sub_node = val, None, None 

class BrokenCalculator:

  def broken_calc(self, x, y): 
    dq = deque() 
    dq.append(MathNode(x)) 

    count = 0

    while True: 
      node = dq.popleft()

      mult_val = node.val * 2 if node.val * 2 < 1000000000 else None
      sub_ val = node.val - 1 if node.val - 1 >= 1 else None


'''
Still haven't solved
'''
      