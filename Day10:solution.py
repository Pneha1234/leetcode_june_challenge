class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first, last = 0, len(nums)
        while first < last:
            mid = (first + last)//2
            if nums[mid] >= target:
                last = mid
            else:
                first = mid + 1
        return first
