from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num]+= 1
        sort_order = sorted(dict1.items(), key=lambda x: x[1], reverse=True) 
        result = []
        counter = 0
        for val in sort_order:
            if counter < k:
                result.append(val[0])
                counter+= 1
        
        return result


        