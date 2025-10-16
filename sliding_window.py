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
        return [maxl,maxr] #Answer is [0,11] which seems to be wrong for now

def main():
    nums=[7,8,12,15,18,20,22,25,30,43,57,72]
    #MaxSum=129
    #0,11
    target=57
    obj=Solution()
    res=obj.sliding_window(nums)
    print("Result:",res)

if __name__=="__main__":
    main()