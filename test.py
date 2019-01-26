def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair): 
	
	return pair()

print(car(cons(3,4)))

