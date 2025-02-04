class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Using sliding window
        l, r = 0, 0

        max_sum = nums[0] # Since we will always have at least one element
        while r < len(nums) - 1:
            if nums[r + 1] > nums[r]:
                r += 1
            else:
                 r += 1
                 l = r
            sub_array = nums[l:r+1]
            max_sum = max(sum(sub_array), max_sum)
        return max_sum
            