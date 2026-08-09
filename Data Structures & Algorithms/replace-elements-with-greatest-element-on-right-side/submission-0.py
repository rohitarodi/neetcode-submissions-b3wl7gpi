class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(1,len(arr)+1):
            if i != len(arr):
                arr[i-1] = max(arr[i:])
            else :
                arr[i-1] = -1
        return arr