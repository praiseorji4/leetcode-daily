# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day13/images/problem.png?raw=true)

# Approach
Used a Minheap to access the minimum value at any given point
- Created a heap out of the array
- Initialized the count
- Used an infinite while loop (since we were told that a solution must exist)
- Check to see if the current min is equal to or greater than the threshold. If so, return the current count
- If not, add the new value as described by the question
- Increase the count.
- Repeat from step 4.

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day13/images/submission.png?raw=true)