class Palindrome:
    def longestPalindrome(self, s: str) -> int:

        sss = set()
        matches = 0

        # loop thorugh string, if ch not in set
        for ch in s:
            if ch in sss:
                sss.remove(ch)
                macthes += 1
            else:
                sss.add(c)
        
        return (matches * 2 + 1) if len(sss) > 0 else return len(s)
        # if no odd len element, then already a palindrome

        # Time: O(n)
        # Space: O(sss.length)