# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day02/images/problem.png?raw=true)

# Approach
- The capacity for any given pair is an 'area of a rectangle' problem.
- The height of any given any given pair is the height of the smaller pair |(as otherwise the water spills).
- The width of any given pair is the difference in their indexes.
- The area is then the product the width and the height.
- I initialized the problem by maximizing width (i.e making the first pair the bars at the extreme ends).
- For optimization, the smaller height was dropped in the next iteration.

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day02/images/submission.png?raw=true)