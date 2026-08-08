class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap :
                hashmap[nums[i]] = 1
            else :
                hashmap[nums[i]] += 1
        print(hashmap)
        max_count = 0
        maj_ele = 0
        for n,count in hashmap.items():
            if count/2 > max_count/2:
                max_count = count
                maj_ele = n
        return maj_ele
