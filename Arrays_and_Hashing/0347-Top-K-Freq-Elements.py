#Solution 1- ssorting - takes nlogn time and n space 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        #stores the list as a Key-Value pair in a hashmap
        for num in nums : 
            mapp[num] = mapp.get(num, 0)+1 


        new_array=[]
        for num, count in mapp.items(): 

            new_array.append([count,num])

        new_array.sort()

        result= []

        while len(result)< k : 
            result.append(new_array.pop()[1])
        

        return result



