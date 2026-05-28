# Day 1 DSA

## Problems Solved

### 1. Two Sum

Implemented:

* Brute force approach using nested loops
* Optimized hashmap approach

### 2. Maximum Element in Array

Implemented:

* Manual traversal approach
* Built-in `max()` approach
* Sorting-based approach

---

## Concepts Learned

### Brute Force

* Checks all possible combinations
* Simpler logic but slower for large inputs
* Often uses nested loops

### Hash Maps

* Store previously seen values for fast lookup
* Avoid repeated searching
* Reduce time complexity significantly

### Traversal

* Iterating through arrays efficiently
* Direct element traversal is often cleaner than index-based traversal

### Safe Initialization

Using:

```python
largest = nums[0]
```

is safer than:

```python
largest = 0
```

because arrays may contain negative numbers.

### Time vs Space Tradeoff

Optimized solutions may:

* use more memory,
* but reduce execution time significantly.

Example:

* Two Sum brute force → O(n²)
* Two Sum hashmap → O(n)

---

## Important Observations

* Not every problem has a “better” optimization.
* Some simple traversal solutions are already optimal.
* Sorting is not always an optimization.
* Readability and correctness matter as much as working output.

---

## Complexity Analysis

### Two Sum

  Approach: 
        Brute Force :
                  Time Complexity: O(n²) 
                  Space Complexity: O(1)
        Hash Map:
                  Time Complexity: O(n) 
                  Space Complexity: O(n)

### Maximum Element

    Approach: 
            Traversal :
                    Time Complexity: O(n) 
                    Space Complexity: O(1)
            Built-in max():
                    Time Complexity: O(n) 
                    Space Complexity: O(1)
            Sorting :
                    Time Complexity: O(n log n) 
                    Space Complexity: O(n)



## Key Takeaways

* Avoid unnecessary repeated computation
* Use hash maps to optimize lookups
* Think about edge cases like negative numbers and empty arrays
* Simpler solutions are often better when already optimal
* Understand *why* an algorithm works instead of memorizing patterns
