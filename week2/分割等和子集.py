class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) %2 ==1:#若和的一半不是偶数，则返回False
            return False
        elif len(nums)==2 and nums[0]==nums[1]: #排除[1,1]的情况
            return True
        else:
            '''
            [1,2,3,4]，half_num=5
            将序列从大到小排序，[4,3,2,1],先把最大的值4放进去sums，从4后面的数里面选择，   4+3>5,则不选3，下一个，4+2>5,跳过下一个，4+1=5,返回True；若遍历到4后面所有的数都不能使4+num[j]=5,则从3开始遍历。
            '''
            nums.sort(reverse=True)
            half_nums = sum(nums)/2
            for i in range(len(nums)):
                sums = nums[i]
                for j in range(i+1,len(nums)):
                    
                    if sums + nums[j] > half_nums:
                        continue
                        
                    elif sums +nums[j] < half_nums:
                        sums = sums +nums[j]
                    else:
                        return True
        return False