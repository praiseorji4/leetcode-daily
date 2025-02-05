# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day05/images/problem.png?raw=true)

# Approach
- The problem is tagged 'easy' so I figured that although it looks like one would have lots of cases to test for, that wouldn't be the case.
- I had to address the simple cases:
	- They can never be the same if they are of different word lengths
	- They can't be the same if they to not have the same letter composition
- Once the above conditions are met, the only thing to check is if the order of the letters differs by at most 2 (a swap fixes two letters at once)

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day05/images/submission.png?raw=true)