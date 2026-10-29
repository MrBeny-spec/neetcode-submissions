class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1 

        a = sorted(d, key=d.get)
        a = a[::-1]
        return a[0:k]
