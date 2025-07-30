# FACTORIAL USING RECURSION

# 0! = 1 
# 1! = 1 (1*1)
# 2! = 2 (1*2)
# 3! = 6 (1*2*3)

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))

result = factorial(5)
print(result)