# 1002. Find Common Characters
from collections import Counter
from functools import reduce

class Solution:
    def commonChars2(self, A):
        cnt_tot = Counter(A[0])
        
        for s in A[1:]:
            cnt_cur = Counter(s)
            cnt_tot &= cnt_cur

        ans = []
        for k, v in cnt_tot.items():
            ans += [k] * v
        return ans

    def commonChars3(self, A):
        cnt_tot = Counter(A[0])
        for s in A:
            cnt_tot &= Counter(s)
        return list(cnt_tot.elements())

    def commonChars(self, A):
        return list(reduce(Counter.__and__, map(Counter, A)).elements())

print(Solution().commonChars(["bella","label","roller"]))