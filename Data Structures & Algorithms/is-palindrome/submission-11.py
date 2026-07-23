class Solution:
    def isPalindrome(self, s: str) -> bool:

        h = 0
        t = len(s) -1
        # this already handles case where array is empty 

        while  h < t: #  they will cross always before invalid index (out of bound)

            while  h < t: 
                h_a =  s[h].isalnum()
                if not h_a:
                    h += 1
                else:
                    break
            
            while  h < t: 
                t_a =  s[t].isalnum()
                if not t_a:
                    t -= 1
                else:
                    break

            if s[h].lower() != s[t].lower():
                return False

            t -= 1
            h += 1

        return True





