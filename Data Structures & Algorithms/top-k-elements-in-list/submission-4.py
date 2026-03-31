class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        # freq = {1:1, 2:2, 3:3}
        output = []
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        #buckets = [[],[],[],[],[],[],[]]
        for num, count in freq.items():
            buckets[count].append(num)
        
        # buckets = [[],[1],[2], [3], [], [], []]
        for i in range(len(buckets)-1, -1, -1):
            for n in buckets[i]:
                output.append(n)
                if len(output) == k:
                    return output