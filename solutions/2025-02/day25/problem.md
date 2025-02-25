# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day25/images/problem.png?raw=true)

# Approach
- Initialize counters for odd and even prefix sums
- Start with even_count = 1 
- Iterate through the array keeping a running sum
- For each element, update the running sum and check its parity
- If current sum is odd, it forms odd-sum subarrays with all previous even prefix sums
- If current sum is even, it forms odd-sum subarrays with all previous odd prefix sums
- Update counters and continue

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-02/day25/images/submission.png?raw=true)