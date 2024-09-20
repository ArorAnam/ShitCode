from collections import Counter
import string

def canConstruct(ransomNote: str, magazine: str) -> bool:
    from collections import Counter
    return not Counter(ransomNote) - Counter(magazine)

def canConstruct(ransonNote, magazine):
    count1 = Counter(ransonNote)
    count2 = Counter(magazine)

    return all(count1[c] <= count2[c] for c in string.ascii_lowercase)
    # return all(count1[c] <= count2[c] for c in [chr(i) for i in range(97, 123)])