class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False  # i가 max_reach를 넘으면 도달할 수 없으므로 False 반환
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1:
                return True  # 최대 도달 범위가 마지막 인덱스를 넘으면 True 반환
        return max_reach >= len(nums) - 1 

s = Solution()
print(s.canJump([2,3,1,1,4]))
            