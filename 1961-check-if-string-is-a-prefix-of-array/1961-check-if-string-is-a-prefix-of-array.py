class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        tempStr = ''
        for st in words:
            print(tempStr)
            tempStr+= st
            if len(tempStr) < len(s):
                if tempStr != s[: len(tempStr)]:
                    return False
            elif len(tempStr) == len(s):
                if tempStr == s: return True
                else: return False
            else: return False
        return False
        