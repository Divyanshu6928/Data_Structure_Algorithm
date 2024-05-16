class Solution:
    def subarraySum(self, a, n):
        t = 0
        mod = 10**9 + 7

        for i in range(n):

            t += a[i] * (i + 1) *(n-i)

        return t % mod