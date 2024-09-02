class Palindrome:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # delete one char from the left and check if the rest of the string is palindrome
                # delete one char from the right and  check if the rest of string is a palindrome
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
            l += 1
            r -= 1
        
        return True

        # Time: O(n)
        # Space: O(n)