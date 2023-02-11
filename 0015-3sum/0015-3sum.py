class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        print(nums)
        for i in range(len(nums)- 2):
            if i != 0 and nums[i] == nums[i - 1]: 
                print(nums[i], nums[i - 1])
                continue
            head = i + 1
            tail = len(nums) - 1
            while head < tail:
                theSame = False
                if head != i + 1 and nums[head] == nums[head - 1]:
                   head+= 1  
                   theSame = True
                if tail != len(nums) - 1 and nums[tail] == nums[tail + 1]:
                   tail-= 1
                   theSame = True
                if theSame: continue
                if nums[i] + nums[head] + nums[tail] == 0:
                    result.append([nums[i], nums[head], nums[tail]])
                    head+= 1
                    tail-= 1   
                elif nums[i] + nums[head] + nums[tail] < 0:
                    head+=1
                else: tail-= 1   
        return result      
                    
                
                
                