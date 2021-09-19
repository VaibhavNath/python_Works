# def fact(n):                      #function method.
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#         return fact
    
def fact_recursive(n):                #recursion method.
    if n==0:
        return 1
    else:
        return n*fact_recursive(n-1)

print(fact_recursive(6))
