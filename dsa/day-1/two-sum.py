# brute force approach
def brute_two_sum(n,a,t):
    # uses two loops for two elements
    for i in range(n):
        for j in range(i+1,n):
          if a[i]+a[j]==t:
             return [i,j]
    return [-1,-1]

#optimal approach
def optimal_two_sum(n,a,t):
    # uses hashmap for reducing time
    h={}
    for i,j in enumerate(a):
        diff=t-j # finding complement for mapping
        if diff in h:
            return [h[diff],i]
        h[j]=i
    return [-1,-1]

n=int(input())
a=list(map(int,input().split()))
t=int(input())
print("Brute force result indices: ",brute_two_sum(n,a,t))
print("Optimal two sum result: ",optimal_two_sum(n,a,t))
