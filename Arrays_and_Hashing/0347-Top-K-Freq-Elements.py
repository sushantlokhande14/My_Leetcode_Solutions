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



# Solution 2- modified bucket sort - time complexity O(n)/ space o(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums : 
            count[num]= count.get(num,0 )+1 
        
        for n,c in count.items(): 
            freq[c].append(n)

        res= []

        for i in range(len(freq)-1, 0 ,-1): # range from end of freqlist , to start . with a step of -1 
            for num in freq[i] : 
                res.append(num)
                if len(res)==k : 
                    return res 
    
