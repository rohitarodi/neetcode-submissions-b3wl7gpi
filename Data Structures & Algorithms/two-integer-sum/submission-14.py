class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def helper(nums,target):
            i = 0
            j = len(nums)-1
            sort_nums = sorted(nums)
            while i<j:
                if sort_nums[i] + sort_nums[j] == target:
                    return [sort_nums[i],sort_nums[j]]
                elif sort_nums[i] + sort_nums[j] > target:
                    j -= 1
                elif sort_nums[i] + sort_nums[j] < target:
                    i += 1
        res = helper(nums, target)
        idx1 = nums.index(res[0])
        idx2 = nums.index(res[1], idx1 + 1) if res[0] == res[1] else nums.index(res[1])
        return sorted([idx1, idx2])