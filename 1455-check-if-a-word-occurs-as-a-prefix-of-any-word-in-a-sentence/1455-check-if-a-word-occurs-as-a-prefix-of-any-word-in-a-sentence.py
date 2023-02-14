class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        length = len(searchWord)
        for sent in sentence:
            if len(sent) >= length and searchWord == sent[:length]: 
                return sentence.index(sent) + 1 
        return -1
            