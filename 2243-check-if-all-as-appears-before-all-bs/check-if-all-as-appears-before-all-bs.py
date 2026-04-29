class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i]=='b':
                if s.find('a',i+1)!= -1:
                    return False
                
            
        return True
       
            
