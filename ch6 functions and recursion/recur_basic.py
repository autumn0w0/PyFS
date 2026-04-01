def show(n):
    if(n==0):  #base case
        return
    print(n)
    show(n-1)
show(5)

#factorial using recursion
def fact(n):
    if(n==0 or n==1):  #base case
        return 1
    return n * fact(n-1)

print(fact(5))