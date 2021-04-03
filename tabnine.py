print("Hello World")

# Program to sort a list

l = [2,5,3,7,4]
l.sort()
print("Sorted ")

# Maximum Profit Problem

n=int(input())
a=[int(x) for x in input().split()]
dp=a.copy()

for i in range(1,n):
    for j in range(i):
        if a[i]%a[j]==0:
            dp[i]=max(dp[i],dp[j]+a[i])
print(max(dp))
