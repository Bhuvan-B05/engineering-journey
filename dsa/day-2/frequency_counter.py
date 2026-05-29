from collections import defaultdict
def freq_count(a):
    f=defaultdict(int) # defaultdict() is ideal for empty dictionary
    for i in a:
        f[i]+=1
    return f #time: O(n), space:O(n)

a=list(map(int,input().split()))
print(freq_count(a))
