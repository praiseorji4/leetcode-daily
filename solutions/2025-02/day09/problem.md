# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day09/images/problem.png?raw=true)

# Approach
The brute force approach comes out to be an O(n^2) solution (i.e finding the bad directly)
Since the number of possible pairs is fixed, I instead found the number of good pairs.
Whole point is that it is easier to calculate good pairs.
For good, if i < j, j - i = nums[j] - nums[i], which can be rewritten as nums[i] - i = nums[j] - j (the 'aha' moment).
As such, we can calculate things in a single iteration.
Each diff is stored in a diff count dict.
For every diff calculated, it forms a pair with EVERY same diff previously found.
Finally, bad pairs aare calculated by finding the difference between total possible pairs and good pairs.


# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day09/images/submission.png?raw=true