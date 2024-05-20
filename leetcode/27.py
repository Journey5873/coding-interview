class Solution(object):
    def removeElement(self, nums, val):
        idx = 0

        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
        return idx

s = Solution()
print(s.removeElement([3,2,2,3], 3))
