class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #algorithm
        # have 2 pointers
        #one pointer at start and one start at end
        #while left < right:
            #check the sum
            #if sum > target :
                #move right pointer to left
            #elif sum < target :
                #move left pointer to right
            #elif sum == target :
                #return true
        #return false
        # nums = [abs(x) for x in nums]
        # target = abs(target)
        # left, right = 0, len(nums)-1
        # while left < right :
        #     sum = nums[left] + nums[right]
        #     if sum > target :
        #         right -= 1
        #     elif sum < target :
        #         left += 1
        #     elif sum == target :
        #         return [left, right]
        # return [] 

        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap :
                return [hashmap[diff], i]
            else :
                hashmap[nums[i]] = i
        return []