from collections import defaultdict
from operator import itemgetter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        minimum = 1
        arr.sort()
        dict1 = defaultdict(int)
        for i in arr:
            dict1[i]+= 1
        print(dict1)
        arr.clear()
        for val in dict1:
            arr.append(dict1[val])
        arr.sort()
        arr.reverse()
        sum = 0
        for val in arr:
            print(val)
            sum+= val
            if sum < length/2:
                minimum+= 1
            else: break
        return minimum
       


