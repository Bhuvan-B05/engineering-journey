# Day 2 DSA

## Problems Solved

### 1. Contains Duplicate

Implemented:

* Brute force approach usig nested loops
* Optimal approach using set

### 2. Frequency Counter

Implemented:

* Used dictionary to store unique elements and their count

### 3. Valid Anagram

* Used two frequency maps and compared them.
* If all characters occur the same number of times, the strings are anagrams.

## Concepts Learned

## Hashing Patterns

### Set
Used for:
- Membership checking
- Duplicate detection

Question:
"Have I seen this before?"

### Dictionary
Used for:
- Frequency counting
- Frequency comparison

Questions:
- "How many times have I seen this?"
- "Do these collections have identical counts?"

## Important Realizations

- Hashing helps avoid repeated searching.
- Not every problem needs nested loops.
- Sets are useful for fast membership checking.
- Dictionaries are useful when information must be stored and reused.
- Time can often be improved by using additional memory.

## Complexity Analysis

### Contains Duplicate
    Approach: 
        Brute Force :
                  Time Complexity: O(n²) 
                  Space Complexity: O(1)
        Set:
                  Time Complexity: O(n) 
                  Space Complexity: O(n)

### Frequency counter
    Approach: 
        Dictionary:
                  Time Complexity: O(n) 
                  Space Complexity: O(n)

### Valid Anagram
    Approach: 
        Dictionaries:
                  Time Complexity: O(n) 
                  Space Complexity: O(n)