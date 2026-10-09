class Solution:
    def isValid(self, s: str) -> bool:
        stack=[];

        for x in s:
            if x in "({[":
                stack.append(x);
            else:
                if not stack:
                    return False;
                temp=x;    
                if x==')':
                    x='(';
                elif x=='}':
                    x='{';
                else:
                    x='[';

                if x!=stack[-1]:
                    return False;
                stack.pop();
        if stack:
            return False;            
        return True;                        
                    