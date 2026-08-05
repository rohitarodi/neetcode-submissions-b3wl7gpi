class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-1):
        #     if nums[i] in nums[i+1:]:
        #         return True
        #     else :
        #         continue
        # return False
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False

        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False





        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        #     else :
        #         continue
        # return False