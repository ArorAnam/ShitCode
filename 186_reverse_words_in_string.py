# Solution 1
 
class Solution:
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
        
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word in the string
            start = end + 1
            end += 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # reverse the whole string
        self.reverse(s, 0, len(s) - 1)

        # reverse each word
        self.reverse_each_word(s)

# Solution 2

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = "".join(s)#the sky is blue
        st_s = st.split()#[the,sky,is,blue]
        st_r = st_s[::-1]#[blue,is,sky,the]
        st_j = " ".join(st_r)#blue is sky the
        s[:] = st_j[::]
        
