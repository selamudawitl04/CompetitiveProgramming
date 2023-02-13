class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        isChanged = False
        for i in range(1, len(arr)):
            if not isChanged and arr[i] <= arr[i - 1]:
                isChanged = True
                if i == 1: return False
                if i == len(arr) - 1 : 
                    if arr[i] < arr[i - 1]: return True
                    else: return False
                continue
            if isChanged and arr[i] >= arr[i - 1]:
                return False             
        return isChanged