class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p_start = 0
        p_curr = 0
        p_end = len(nums) - 1

        while p_curr <= p_end:
            if nums[p_curr] == 0:
                nums[p_start], nums[p_curr] = nums[p_curr], nums[p_start]
                p_start += 1
                p_curr += 1
            elif nums[p_curr] == 2:
                nums[p_curr], nums[p_end] = nums[p_end], nums[p_curr]
                p_end -= 1
            else:
                p_curr += 1