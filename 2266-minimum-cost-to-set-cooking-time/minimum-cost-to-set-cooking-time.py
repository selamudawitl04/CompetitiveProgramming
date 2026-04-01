class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        # Create the ways
        def doCost(minute, second)-> int:
            string = ''

            if minute > 0:
                string = str(minute)

            if len(str(second)) == 1:
                if minute > 0:
                    string = string + '0' + str(second)
                else:
                    if second != 0:
                        string = str(second)

            else:
                string = string + str(second)


            print(string)
            cost = 0
            if string[0] != str(startAt) :
                cost+= moveCost

            for i in range(1, len(string)):
                # Calculate move cost
                if string[i] != string[i - 1]:
                    cost+= moveCost
            
            return cost + len(string) * pushCost

        minutes = targetSeconds // 60
        seconds = targetSeconds - minutes * 60

        print(minutes, seconds)

        minCost = math.inf
        if minutes < 100:
            minCost = doCost(minutes, seconds)
            
        if 60 + seconds < 100  and minutes > 0:
            minCost = min(minCost, doCost(minutes - 1, seconds + 60))

        return minCost


