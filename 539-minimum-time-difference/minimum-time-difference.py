from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Sort the time points
        timePoints.sort()
        n = len(timePoints)
        minValue = 24 * 60  # maximum possible difference in minutes

        for i in range(n):
            # Current time in minutes
            h1, m1 = map(int, timePoints[i].split(":"))
            t1 = h1 * 60 + m1

            # Next time in minutes (wrap around for circular difference)
            h2, m2 = map(int, timePoints[(i + 1) % n].split(":"))
            t2 = h2 * 60 + m2

            # Difference in minutes
            diff = (t2 - t1) % (24 * 60)
            minValue = min(minValue, diff)

        return minValue