class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n

        # Left
        prefix[0]=1
        for i in range(1,n):
            prefix[i]=prefix[i-1] * nums[i-1]

        # Right
        suffix[n-1]=1
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1] * nums[i+1]

        ans=[]
        for i in range(n):
            nums[i]=prefix[i] * suffix[i]
            ans.append(nums[i])
        
        return ans