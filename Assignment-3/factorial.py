n = int(input("Enter a number: "))      #ask the user to enter a number!

def factorial(n):
    if n < 2:
        return 1                        
    else:
        return n * (factorial(n-1))     #returns the factorial of the number using recursion
    
result = factorial(n)
print(f"Factorial of {n} is:",result)   #f-string for clean and readable formatting