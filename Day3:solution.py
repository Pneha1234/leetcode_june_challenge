class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs)//2
        minimal_cost = 0
        diff_a, diff_b = [], []

        for cost in costs: 
            if cost[0] < cost[1]:  
                minimal_cost += cost[0]   
                diff_b.append(cost[1]-cost[0])  
            else:                 
                minimal_cost += cost[1]
                diff_a.append(cost[0]-cost[1])

        if len(diff_a) < len(diff_b): 
            diff_b.sort()
            for j in range(len(diff_b)-N):
                minimal_cost += diff_b[j]

        if len(diff_a) > len(diff_b):  
            diff_a.sort()
            for i in range(len(diff_a)-N):
                minimal_cost += diff_a[i]

        return minimal_cost
