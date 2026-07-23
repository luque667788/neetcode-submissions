class Solution:
    def isPalindrome(self, s: str) -> bool:

        h = 0
        t = len(s) -1
        # this already handles case where array is empty 

        while  h < t: #  they will cross always before invalid index (out of bound)

            while  h < t and not s[h].isalnum(): 
                h += 1

            
            while  h < t and not s[t].isalnum(): 
                t -= 1


            if s[h].lower() != s[t].lower():
                return False

            t -= 1
            h += 1

        return True





