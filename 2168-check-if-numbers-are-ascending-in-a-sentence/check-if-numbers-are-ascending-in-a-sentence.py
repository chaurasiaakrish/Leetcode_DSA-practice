class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        s=s.split()
        for i in s:
            if i.isdigit():
                l.append(int(i))
        if l==sorted(l):
            if len(l)==len(set(l)):
                return True
            else:
                return False    
        else:
            return False  