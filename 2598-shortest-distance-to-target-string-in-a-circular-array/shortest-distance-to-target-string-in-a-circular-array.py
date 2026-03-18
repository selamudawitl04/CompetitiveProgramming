
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        result = float('inf')

        for i in range(n):
            if words[i] == target:
                # circular distance
                dist = abs(i - startIndex)
                result = min(result, dist, n - dist)

        return result if result != float('inf') else -1