class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(i) for i in num]
        string = "".join(num)
        string = str(int(string) + k)
        num = str(int(string));
        print(num)
        return [int(i) for i in num]