
# Solution 1 - timecomplexiety - m X nlogn  , space - m X n , solution using sorting 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs: 

            sorted_s = ''.join(sorted(s))
            res[sorted_s].append(s)

        return list(res.values())

# Solution 2  using counting , Time compliexiry  m X n ,  
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs :

            count = [0] * 26 

            for char in s: 

                count[ord(char) - ord("a")]+=1 

            res[tuple(count)].append(s)

        return list(res.values())
        



