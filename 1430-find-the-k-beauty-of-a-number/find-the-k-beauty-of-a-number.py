class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        left = 0
        right = k 

        num_string = str(num)

        length  = len(num_string)

        k_beauty = 0


        while right <= length:
            sub_string = num_string[left : right]
            int_value = int(sub_string)
            
            if int_value != 0 and num % int_value == 0:
                k_beauty+= 1

            left+= 1
            right+= 1

        
        return k_beauty

        