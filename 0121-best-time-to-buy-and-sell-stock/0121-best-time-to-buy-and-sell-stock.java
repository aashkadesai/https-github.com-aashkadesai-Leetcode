class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int i = 0, j = 1;
        
        while(j < prices.length) {
            if(prices[i] < prices[j]) {
                int profit = prices[j] - prices[i];
                max_profit = Math.max(max_profit, profit);
            } else i = j;
            j++;
        }
        return max_profit;
    }
}