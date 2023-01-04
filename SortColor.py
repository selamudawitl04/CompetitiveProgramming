class Solution:
    def sortColors(self, nums: List[int]) -> None:
        head = 0
        tail = len(nums) - 1
        index = 0
        while(index <= tail):
            if nums[index] == 0:
                nums[index] = nums[head]
                nums[head] = 0
                head+= 1
                index+= 1
            elif nums[index] == 2 :
                nums[index] = nums[tail]
                nums[tail] = 2
                tail-= 1
            else: index+= 1


        """
        Do not return anything, modify nums in-place instead.
        """
