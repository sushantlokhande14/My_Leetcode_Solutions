

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs: 
            res+= str(len(s))+ "#" + s 
        
        return res

