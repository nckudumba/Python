# 2 numbers, if you add then = 7
# square of the number
# 1 function call to be used

# def exec(x,y):
#     z = x + y
#     r = pow(z,2)     

# exec(5,2)

def add(x,y):
    return x + y # 5 + 2 = 7
def square(z):        
    return z * z # 7 * 7 = 49

result = square(add(5,2))   # assign the variable square to result
print(result)    # print the answer 49
    