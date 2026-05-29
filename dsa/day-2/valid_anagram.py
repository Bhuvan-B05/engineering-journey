from collections import defaultdict
def valid_anagram(s,t):
    if len(s)!=len(t): # if different lengths then cannot be anagrams
        return False
    # frequency maps for strings s,t
    fs=defaultdict(int) 
    ft=defaultdict(int)
    for i in range(len(s)):
        # add count 1 for every unique element
        fs[s[i]]+=1
        ft[t[i]]+=1
    if fs==ft: # if moth maps are equal then anagrams
        return True
    return False
s=input()
t=input()
print(valid_anagram(s,t))