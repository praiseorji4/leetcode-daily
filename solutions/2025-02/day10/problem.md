# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day10/images/problem.png?raw=true)

# Approach
- I immediately thought of using a stack as soon as I saw that there would be a distinction between digits and non-digits
- If the current element is a non-digit, it would be placed on top of the stack.
- if the current element is a digit, we pop from the stack as the top element would represent the closest non-digit to the left
- The answer becomes what is left in the stack after the loop.

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day10/images/submission.png?raw=true)