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
