class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for _ in range(len(nums1) - m):
            nums1.pop()
        nums1 += nums2
        nums1.sort()

solution = Solution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))