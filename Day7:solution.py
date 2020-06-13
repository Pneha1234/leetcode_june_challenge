class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        S = [(((1<<(32*(amount//i*i + i)))) - 1)//((1<<(i*32)) - 1) for i in coins]
        prodd = 1
        
        for i in S: prodd = (prodd * i) & ((1<<((amount +1)*32))-1)
        return prodd>>(32*amount)
