class Solution:
    def binarySearch(self, nums, mid, low, high, target)->int:
        if low > high :
            return mid + 1
        if nums[mid] == target: return mid
        elif nums[mid] < target:
            low = mid + 1
            mid = (high + low) // 2
            return  self.binarySearch(nums, mid, low, high, target)
        else:
            high = mid - 1
            mid = (high + low) // 2
            return self.binarySearch(nums, mid, low, high, target)
         
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = high//2
        return self.binarySearch(nums, mid, low, high, target)
   

