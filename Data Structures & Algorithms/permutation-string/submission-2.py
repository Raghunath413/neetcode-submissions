class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check=sorted(s1);
        k=len(s1);
        start=0;
        end=k-1;
        n=len(s2);
        while start -k<n and end <n:
            temp=s2[start:end+1];
            t=sorted(temp);
            if t==check:
                return True;
            start +=1;
            end +=1;    
        return False;
        