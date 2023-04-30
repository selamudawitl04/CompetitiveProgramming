class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.split(" ");
        length = len(s) - 1;
        while length >= 0:
            if s[length] != '':
                return len(s[length])
            length-= 1
        
        return 0