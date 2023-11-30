class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices={}
        for ind, key in enumerate(nums):
            if (key in indices and ind-indices[key] <=k):
                return True
            indices[key]=ind
        return False        