# Remember all your stuff and where it goes in a function 

# my_str.replace(s1, s2) replaces all instances of s1 in my_str with s2 and RETURNS IT since strings are immutable in Python, it does not change my_str itself

# replace string with nothing
x = "(()))"
while "()" in x:
  x = x.replace("()", "")

print(x) # output is )

# replace string with another string
x = "hello world"
z = x.replace("l", "y")
print(z) # outputs "heyyo woryd"
print(x) # outputs "hello world"
