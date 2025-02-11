# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day11/images/problem.png?raw=true)

# Approach
Seeing as this involves in-place modification of a string, using a stack came to mind.
- Initialize the stack.
- Get the length the substring.
- Fill the stack and if the stack has contents equal to the size of the substring, check if the substring forms the top of the stack.
- If so, pop from the stack until the entire substring is gone.
- Return the contents of the  stack as a string.

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day11/images/submission.png?raw=true)