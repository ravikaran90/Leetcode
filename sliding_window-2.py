class Solution:
    def sliding_window(self,nums):
        maxsum=nums[0]
        cursum=0
        l=0
        maxl,maxr=0,0

        for r in range(len(nums)):
            if cursum<0:
                cursum=0
                l=r
            cursum+=nums[r]
            if maxsum<cursum:
                maxsum=cursum
                maxl,maxr=l,r
        return [maxl,maxr]

def main():
    nums=[4,-1,2,-7,3,4]
    obj=Solution()
    res=obj.sliding_window(nums)
    print("Result:",res)

if __name__=="__main__":
    main()