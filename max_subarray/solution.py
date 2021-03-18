class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    # Here I implement Kadane's algorithm. I set a local max value to track the local maximum of the subarrays,
    # and then I update the global max each time I find a new local maximum for a given subarray.
        local_max = 0
        # The global max is set to the minimum value to account for negative numbers in the sample data sets.
        global_max = -(10**5) - 1
        n = len(nums)
    
        # The minimum array size is 1, so I handle this edge case first. The maximum subarray in that case
        # would just be the one value in the array.
        if n == 1:
            return nums[0]
        
        # Loop through the nums array and find the local max, which is either the previous local max plus the
        # current array element, or the current element is the new maximum. I then determine what the new global
        # max is, either the previous global max or the new local maximum.
        for i in range(n):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)
        
        # Return the global maximum
        return global_max