#def func():
#   statements
#   .....
#   return (expr)

#function call

#.................

def add(a,b):
    print(a+b)

add(1,2)

#..................

def add1(a,b):
    c = a+b
    return c

ans = add1(10,20)   # we have to assign the function call so that we can print the output!
print(ans)

def mult(a,b):
    c = a * b
    return c

result=mult(2, 'Mike ')
print(result)