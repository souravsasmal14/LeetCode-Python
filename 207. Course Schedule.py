class Solution:
    def canFinish(self, n: int, preq: List[List[int]]) -> bool:
        hm = { i: [] for i in range(n)}
        vs = set()
        for c,p in preq :
            hm[c].append(p)
        def dfs(c):
            if c in vs:
                return False
            if hm[c] == []:
                return True
            vs.add(c)
            for p in hm[c]:
                if not dfs(p): return False
            vs.remove(c)
            hm[c] =[]
            return True
        for c in range(n):
            if not dfs(c):
                return False
        return True                                