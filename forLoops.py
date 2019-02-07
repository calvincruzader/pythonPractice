# for loops iterate over iterables
for i in range(10):
	print("{} ".format(i), end='')
print()
for i in [1, 2, 3, 4]:
	print("{} ".format(i), end='')		
print()
for c in 'hello': 
	print("{} ".format(c), end='')
print()
for x in ('a', 1, 'b', 3, 'c'): 
	print("{} ".format(x), end='')
print()
for x in [(1,2), 4, ('c', 6), 'd']:
	print("{} ".format(x), end='')