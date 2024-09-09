
def findRepeatedDnaSequences(s: str) -> list[str]:
    if len(s) < 10:
        return []
    
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        substring = s[i:i+10]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)
    
    return list(repeated)
    
# testcase - 1
print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # ["AAAAACCCCC","CCCCCAAAAA"]

# testcase - 2
print(findRepeatedDnaSequences("AAAAAAAAAAAAA")) # ["AAAAAAAAAA"]

# Time complexity: O(n) where n is the length of the input string s
# Space complexity: O(n) where n is the length of the input string s
