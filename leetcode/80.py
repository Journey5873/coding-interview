class Solution(object):
    def removeDuplicates(self, nums):
        num_dic = {}

        idx = 0
        for num in nums:
            if not num in num_dic:
                num_dic[num] = 1
                nums[idx] = num
                idx += 1
            else:
                if num_dic[num] < 2:
                    num_dic[num] +=1
                    nums[idx] = num
                    idx += 1
        return idx
    
nums = [1,1,1,2,2,3]
s = Solution()
print(s.removeDuplicates(nums))
print(nums)