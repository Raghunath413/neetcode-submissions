class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans=nums[0];
        for x in nums:
            ans=min(ans,x);

        return ans    
        