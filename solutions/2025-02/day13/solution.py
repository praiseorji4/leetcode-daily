import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Since we are dealing with getting minimum values, I will use a min heap
        count = 0
        heapq.heapify(nums)

        while True: # Since we've been assured that there would always be a solution
            # Get the first minimum
            min1 = heapq.heappop(nums)
            if min1 >= k:
                return count

            # Get second minimum
            min2 = heapq.heappop(nums)

            # Push the defined value into the heap
            val = min(min1, min2) * 2 + max(min1, min2)
            heapq.heappush(nums, val)
            
            # Update Count
            count += 1
            
            