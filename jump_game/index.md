Reference: https://leetcode.com/problems/jump-game-ii/

## About the Puzzle
Jump Game II is an exercise from leetcode.com and the link to the puzzle can be found in the beginning of this page. No further history about the problem was found until now.

## Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index i. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

   - `0 <= j <= nums[i] and`
   - `i + j < n`

Return the minimum number of jumps to reach `nums[n - 1]`. In other words, return the minimum number of jumps to reach the last index of the array.

### Aditional Information
- It is guaranteed that you can always reach the last index.
- You can only jump to the right. 

**Constraints:**

- 1 <= `nums.length` <= 10^4
- 0 <= `nums[i]` <= 1000

**Example 1:**
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.   
Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**
```
Input: nums = [2,3,0,1,4]
Output: 2
```
### Hints
1. Make it work for a simple example. `nums = [1,1,1,1]`, what is the minimum number of jumps to reach the last index?
2. Now improve it for a more complex example. `nums = [2,3,1,1,4]`.
3. There is a BFS solution. Can you find it?
4. You can also solve this one with dynamic programming.
5. The most optimal solution involves only one loop. Can you find it? 

## Solutions

### Solution 1: BFS
`Time Complexity: O(n^2)`
`Space Complexity: O(n)`

This solution is probably the most intuitive one. Once we have at least once solved another exercises with this approach. 
The steps to solve with this approach are:
1. Create a queue and add the first element to it.
2. While the queue is not empty:
    1. Pop the first element from the queue.
    2. If the element is the last one, return the number of jumps.
    3. Add all the possible jumps to the queue.
    4. Increment the number of jumps.

### Solution 2: Greedy Algorithm (leetcode Optimal Solution)  
`Time Complexity: O(n)`  
`Space Complexity: O(1)`  
This solution is based on the fact that we can always reach the last index.  
The steps to solve with this approach are:  
1. Create three variables to store the current maximum index we can reach, to store the next maximum and one for the number of jumps.  
2. Iterate over the array.  
3. If the current index is greater than the next maximum, update the next maximum and increment the number of jumps.  
4. Return the number of jumps.  

### Solution 3: Dynamic Programming extra challenge  
Having implemented the two previous solutions, can you implement this one?  
