
## About the Puzzle  
Longest Substring is an exercise from leetcode.com and the link to the puzzle can be found in the beginning of this page. No further history about the problem was found until now.  
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Longest Substring Without Repeating Characters  

Given a string s, find the length of the longest substring without repeating characters.  

 
**Constraints:**

- 0 <= `s.length` <= `5 * 104`  
- `s` consists of English letters, digits, symbols and spaces.  

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.  
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.  
```

## Hints
1. Make it work for a simple example. `s = "abcabcbb"`, what is the longest substring without repeating characters?  
2. Now improve it for a more complex example. `s = "pwwkew"`.  
3. Can you make it better than `O(n*m)` time complexity?  

## Solutions

### Solution: Brute Force
`Time Complexity: O(n*m)`  
`Space Complexity: O(n)`  
This solution is probably the most intuitive one and the steps to solve with this approach are:  
1. Iterate over the string. Saving the current character in a variable.  
2. Iterate over the string again, starting from the current character. Stoping when a repeated character is found.  
3. If the length of the substring is greater than the current longest substring, save it.  

### Solution: Sliding Window 
This solution can be found here: https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/  

`Time Complexity: O(n+d)`  
`Space Complexity: O(n)`  
The Sliding Window approach is a very common one. The steps to solve with this approach are:  
1. Create a set to save the characters of the current substring.  
2. Create a variable to save the current longest substring.  
3. Create two pointers, one to the start of the substring and another to the end of the substring.  
4. Iterate over the string.  
    4.1. If the current character is not in the set, add it to the set and move the end pointer to the right.  
    4.2. If the current character is in the set, remove the character at the start pointer from the set and move the start pointer to the right.  
    4.3. If the length of the current substring is greater than the current longest substring, save it.  

### Function Signature
Implement any of the solutions in Python and submit it here. Your function must use the following declaration:  

```python
    def one_edit_away(first: str, second: str) -> bool:
        pass
```
### Most Common mistakes
During the interviews the most common mistakes were:  
1. Understanding of the problem, sometimes people would just start coding and not actually simulating first. As an attempt to solve fast.  
2. Missing the fixes for edge cases in their final solution.  
3. Not finding the proper structure to save the necessary data.  

### General Problems
1. People would find the intuitive brute force solution pretty fast, but would not try to optimize it. Just a single interviewee went for a fast O(n) solution.  

### Identifying positive and negative points in interviewees
First I would like to point out that also by interviewing multiple times I got better in explaining the problem so as I mentioned before sometimes people would not simulate enough so that they would get a proper understanding of what the problem actually was. Second, as interviews came by it was clear that everyone could make the O(n^2) solution but not everyone was able or even intended to make it better.    
Also people that took longer to find the O(n^2) solution intended to stop in that solution, while people that found it fast would accept the challenge to find a more optimal solution.  

### What called my attention
The things that called my attention were:  
1. A divergent solution which iterated 0-n and also n-0, that implementation was completely disruptive and also looked good in time and space complexity. But when simulating it ends up failing with a specific set of inputs.  
2. How fast some people are in changing their approach when intrigued to find a more optimal solution. I thought that people would just give up after finding a good solution. But some of them actually tried to find the very best taking up to 50 minutes in that search. Some actually found it.  
