class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
               
        for i in strs:
            keys=''.join(sorted(i))
            seen[keys].append(i)
        return  list(seen.values())

    



