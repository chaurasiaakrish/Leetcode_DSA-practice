class Solution:
    def isPalindrome(self, x: int) -> bool:
        copy_x=x
        rev_x=0
        rem=0
        abs_x=abs(x)
        if abs_x==x:
            while x>0:
                rem=x%10 #2
                x=x//10 #1
                rev_x=rem+rev_x*10 # 2+10
            if copy_x==rev_x:
                return True
            else:
                return False
        else:
            return False                
        