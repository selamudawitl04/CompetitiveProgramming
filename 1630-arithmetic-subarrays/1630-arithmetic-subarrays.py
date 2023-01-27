class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            arr = nums[l[i] : r[i] + 1]
            arr.sort() 
            print(arr)
            temp = arr[1] - arr[0]
            flag = True
            for j in range(len(arr) - 1):
                if arr[j + 1] - arr[j] != temp:
                    flag = False
                    break
            result.append(flag)
        return result        
