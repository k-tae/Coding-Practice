def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans

n,k=map(int,input().split())
print(factorial(n-1)//(factorial(k-1)*factorial(n-k)))