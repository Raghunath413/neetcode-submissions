class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mp={};
        index=0;
        n=len(s);
        count=0;
        start=0;
        ans=0;
        while index <n and start <=index:
            mp[s[index]]=mp.get(s[index],0)+1;
        
            count=max(count,mp[s[index]]);
            while (index -start +1)-count > k:
                mp[s[start]] -=1;
                start +=1;

            ans=max(ans,index-start+1);
            index +=1;
        return ans;                 
