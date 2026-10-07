class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s);

        mp={};
        start=0;
        end=0;
        ans=0;
        while start<=end and end < len(s):
            if mp.get(s[end],0) >0:
                while s[start]!=s[end]:
                    mp[s[start]] -=1;
                    start +=1;
                start +=1;    
            else:
                mp[s[end]] =mp.get(s[end],0)+1;        
            end +=1;
            ans=max(ans,(end-start))

        return ans;