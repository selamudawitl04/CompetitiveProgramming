class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        n = len(colors)

        count = 0

        for i in range(n):
            left = i - 1
            right = (i + 1) % n

            if colors[left] == colors[right] and colors[left] != colors[i]:
                count+= 1
        
        return count

        

        