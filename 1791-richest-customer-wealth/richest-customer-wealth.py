class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0     
        for i in range(len(accounts)):
            current_customer_wealth = 0
            for j in range(len(accounts[i])):
                current_customer_wealth += accounts[i][j]
            max_wealth = max(max_wealth, current_customer_wealth)           
        return max_wealth