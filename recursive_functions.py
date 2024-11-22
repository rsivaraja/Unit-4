def sum():
    n=10
    for i in range(10):
        n=n+i
        print(n)


sum()
def sum(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return n+sum(n-1)
    
print(sum(5))