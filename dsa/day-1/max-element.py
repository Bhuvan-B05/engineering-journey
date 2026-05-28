"""
Find the largest element in an array using different approaches.

Concepts:
- Traversal
- Safe initialization
- Time complexity
- Mutation awareness
"""


def optimal_largest1(a):
    # Initialize with first element to safely handle negative values
    largest=a[0] 
    for i in a[1:]:
        if largest<i: # compares current largest and element
            largest=i
    return largest # time complexity: O(n), space: O(1), optimal and simple

def built_in_largest(a):
    # uses built-in function
    return max(a) # time: O(n), space: O(1), works but uses built-in

def sort_largest(a):
    # sorting array
    return sorted(a)[-1] # return last element , time: O(n log n), space: depends, # Sorting works but performs unnecessary extra work compared to traversal

a=list(map(int,input().split()))
print("Optimal Approach especially handling negative cases: ",optimal_largest1(a))
print("Optimal Approach using built-in function: ",built_in_largest(a))
print("Optimal approach using sorting: ",sort_largest(a))