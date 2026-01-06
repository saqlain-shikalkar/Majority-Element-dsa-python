# Majority Element Finder (Boyer–Moore Algorithm)

## 📌 Problem Statement
Given an array of integers, find the element that appears more than ⌊N/2⌋ times.
If no such element exists, return -1.

---

## 🚀 Approach
This solution uses the **Boyer–Moore Voting Algorithm**:
- Cancels out different elements
- Guarantees finding the majority element if it exists

---

## 🧠 Algorithm Steps
1. Maintain a `candidate` and `count`
2. Increment count if same element appears
3. Decrement count for different elements
4. Verify the final candidate


## 💻 Python Implementation

```python
def majorityElement(arr, n):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > n // 2:
        return candidate
    return -1

arr=[2,2,1,2,2]
print(majorityelement(arr,len(arr)))


# Output:
# 2


def majorityelement(arr, n):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num

arr=[2,2,1,2,2]
n=len(arr)

result=majorityelement(arr,n)
print(result)

# Output:
# 2


## 💻 Complexity

🟢 Easy

Two Sum

Find Duplicate in Array

Move Zeros

Maximum Subarray (Kadane’s Algorithm)

🟡 Medium

Majority Element II

Subarray Sum Equals K

Longest Consecutive Sequence

Rotate Array

🔴 Important Patterns

Hash Map

Two Pointers

Sliding Window

Boyer–Moore

Prefix Sum

👉 Practicing these = 90% interview coverage
