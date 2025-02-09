from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Whole point is that it is easier to calculate good pairs.
        # For good, if i < j, j - i = nums[j] - nums[i], which can be rewritten as...
        # nums[i] - i = nums[j] - j
        diff_count = defaultdict(int)
        good_pairs = 0
        
        # calculate nums[i] - i for each number
        for i, num in enumerate(nums):
            diff = num - i

            # if we've seen a particular diff, 
            # each new one that comes in forms a pair with EACH of the previous
            good_pairs += diff_count[diff]

            # increase the count of this diff found
            diff_count[diff] += 1
            
        n = len(nums)
        # total possible pairs is given by the formula
        total_pairs = (n * (n-1)) // 2
        
        # bad pairs = total pairs - good pairs
        return total_pairs - good_pairs