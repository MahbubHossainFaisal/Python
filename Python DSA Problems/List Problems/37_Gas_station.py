class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_cost>total_gas:
            return -1

        current = 0
        start=0
        for i in range(len(gas)):
            current += gas[i]-cost[i]

            if current<0:
                start = i+1
                current=0

        return start