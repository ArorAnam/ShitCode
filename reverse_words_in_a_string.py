class Solution:
    # Time: O(n)
    # Space: O(n)
    def reverseWords(self, s: str) -> str:
        return " ".join((reversed(s.split())))

    # Time: O(n)
    # Space: O(n)
    def reverseWords(self, s: str) -> str:
        '''
        trim the spaces and convert string into array
        reverse the whole array
        reverse each word
        join
        '''
        ans = []
        i, n = 0 , len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i < n:
                j = i
                while j < n and s[j] != ' ':
                    j += 1
                ans.append(s[i:j])
                i = j
        return ' '.join(ans[::-1])


    # Deque of words
    # Time: O(n)
    # Space: O(n) -- dependent on the words in the string
    from collections import deque
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1
        
        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1
        
        dq, word = deque(), []
        # push word by word into the deque
        while left <= right:
            if s[left] == ' ' and word:
                dq.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        dq.appendleft(''.join(word))

        return ' '.join(dq)


def reverse_words(s):
    words = s.strip().split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Example usage
s = "Your example sentence here"
result = reverse_words(s)
print(result)