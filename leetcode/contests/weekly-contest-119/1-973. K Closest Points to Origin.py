class Solution:
    # Accepted
    def kClosest(self, points, K):
        dist = []
        for p in points:
            dist.append((p[0]**2 + p[1]**2, p))
        dist.sort()
        ans = []
        for d in dist[:K]:
            ans.append(d[1])
        return ans

sol = Solution()
print(sol.kClosest(points = [[1,3],[-2,2]], K = 1))
print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))
