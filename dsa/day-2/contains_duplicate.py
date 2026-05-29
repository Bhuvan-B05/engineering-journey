#brute force
def brute_contains_duplicate(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):# compare each element with every other element next
            if a[i]==a[j]:# if any two equal
                print("Conatin Duplicate: ",a[i]) # print the duplicate
                return
    print("No duplicates") # time: O(n^2), space: O(1)

# optimal approach
def optimal_contains_duplicate(a):
    s=set() # set to store seen elements
    for i in range(len(a)):
        if a[i] in s: # if already seen
            print("Contains Duplicate: ",a[i]) # then it is a duplicate
            return
        s.add(i) # add if not seen
    print("No duplicates") # time: O(n), space: O(k) to O(n) where k is no of unique elements 

a=list(map(int,input().split()))
brute_contains_duplicate(a)
optimal_contains_duplicate(a)