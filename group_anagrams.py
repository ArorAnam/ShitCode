class Anagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l)-ord('a')] += 1
            res[tuple(count)].append(s)
        
        return res.values()

        # Time: O(m * n * 26)
        # Space: O()

    # not using defualt dict


    def groupAnagrams(strs):
        res = {}
        for s in strs:
            count = [0] * 26 # a .... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        
        return list(res.values())