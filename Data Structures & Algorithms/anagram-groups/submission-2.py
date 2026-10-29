class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        a = []
        c = 0
        for i, ss in enumerate(strs):
            temp = "".join(sorted(ss))
            
            if temp not in dic.keys():
                dic[temp] = c
                c += 1
                a.append([ss])
            else:
                a[dic[temp]].append(ss)
        return a

             
                
                
            