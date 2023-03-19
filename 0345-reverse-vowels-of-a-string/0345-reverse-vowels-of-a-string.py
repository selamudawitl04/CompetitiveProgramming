class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        s = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] in vowel and s[right] in vowel:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left+= 1
                right-= 1
            elif s[left] in vowel:
                right-= 1
            elif s[right] in vowel:
                left+= 1
            else:
                left+= 1
                right-= 1
        s = ''.join(s)
        return s
                