items = [1,2,3,4,5]

squared = list(map(lambda x: x ** 2, items))

print(items)
print(squared)


def explicit_function_double(x): 
  return x * 2 

doubled = list(map(explicit_function_double, items))

print(doubled)