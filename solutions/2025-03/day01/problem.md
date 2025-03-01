# Problem
![Problem Description](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-03/day01/images/problem.png?raw=true)

# Approach
- Iterate through the array from the beginning to the second-to-last element (index 0 to n-2)
- At each index i, compare nums[i] with nums[i+1]
- If they are equal, multiply nums[i] by 2 and set nums[i+1] to 0
- After completing all operations, move all zeros to the end
- To shift zeros efficiently, collect all non-zero elements in a new array
- Then append the correct number of zeros to match the original array length
- Return the resulting array

# Solution
![Submission Results](https://github.com/praiseorji4/leetcode-daily/blob/main/solutions/2025-03/day01/images/submission.png?raw=true)