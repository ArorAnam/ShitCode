class Plaindrome:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
            left += 1
            right -= 1
        return True

    def isPalindrome():
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True


        # Time: O(N)
        # Space: O(1)

    def isPlaindrome2():
        #''.join() ; char.isalnum() ; s.lower() ; s[::-1]
            s = ''.join(char for char in s if char.isalnum())
            s = s.lower()
            reversed_s = s[::-1]
            return s == reversed_s

    def isPalindrome3():
        alphabets = "abcdefghijklmnopqrstuvwxyz0123456789"
        sx = [*s.lower()]
        new_str = []
        for i in sx:
            
            if i in alphabets:
                new_str.append(i)
        
        new_str = "".join(new_str)
              
        if new_str  == new_str[::-1]:
            return True
        else:
            return False 