class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Rule 1: total gas must be enough
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        # Rule 2: greedy scan
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                # cannot start from any station <= i
                start = i + 1
                tank = 0

        return start
