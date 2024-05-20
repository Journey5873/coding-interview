class Solution(object):
    def majorityElement(self, nums):
        majority_num = len(nums)//2
        num_dic = {}

        for num in nums:
            if num in num_dic:
                num_dic[num] += 1
            else:
                num_dic[num] = 1
            
            if num_dic[num] > majority_num:
                return num
        return 0
s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))