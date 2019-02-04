x = [1,2,3]

def testWhileElse(x, val_to_find): 

	idx = 0 
	while idx < len(x): 
		if x[idx] == val_to_find: 
			break 
		idx += 1
	else: 
		x.append(val_to_find)
		print("{} was not in the original array of {}".format(val_to_find, x))

print("else statements in loops only execute if the loop terminated without breaks.")
val_to_find = 4
print("val_to_find = {}".format(val_to_find))
print()