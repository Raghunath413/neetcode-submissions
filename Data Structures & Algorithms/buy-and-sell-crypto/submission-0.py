class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxbenifit=0;
        currentbuy=prices[0];
        for x in prices:
            currentbuy=min(currentbuy,x);
            maxbenifit=max(maxbenifit,(x-currentbuy));
        return maxbenifit;    
        