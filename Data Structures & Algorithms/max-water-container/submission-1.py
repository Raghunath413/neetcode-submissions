class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1;
        left=0;
        ans=0;
        while left <right:

            height=min(heights[left],heights[right]);
            ans=max(ans,(height*(right-left)));
            if heights[left]<heights[right]:
                left+=1;
            else:
                right-=1;
        return ans;            

        