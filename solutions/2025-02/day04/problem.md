# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day04/images/problem.png?raw=true)

# Approach
Since this involves sub arrays, I thought to use a sliding window.
From the constraints, we know that 'nums' will never be empty. As such, the initial max sum can be the first element.
It then becomes a sliding window problem with the window reinitializing once the increasing condition is violated.

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day04/images/submission.png?raw=true)