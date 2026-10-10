class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxsize=piles[0];
        minsize=1;
        for x in piles:
            maxsize=max(maxsize,x);

        ans=maxsize;    
        while minsize <= maxsize:
            stepsize=minsize +(maxsize - minsize)//2;
            count=0;
            for x in piles:
                count += (x + stepsize - 1) // stepsize;
            if count <= h:
                ans=min(ans,stepsize);
                maxsize=stepsize -1;
            else:
                minsize=stepsize +1;

        return ans;                   
