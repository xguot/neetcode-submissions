class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cnt = Counter(nums)

        ans = [x for x, count in cnt.most_common(k)] 

        return ans