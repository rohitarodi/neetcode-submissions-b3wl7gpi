class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # count = 0
        # original_list = nums.copy()
        # for i in original_list :
        #     value = nums.pop(nums.index(i))
        #     if value in nums: 
        #         count += 1
        # if count >= 1 :
        #     return True
        # else:
        #     return False
        if len(set(nums)) < len(nums) :
            return True
        else :
            return False