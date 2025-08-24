class Solution: 
    def two_sum(self,nums,target):
        diction={}
        for i in range(len(nums)):
            compl=abs(nums[i]-target)
            if compl in diction:
                return [diction[compl],i]
            diction[nums[i]]=i

def main():
    nums=[2,7,11,15]
    obj=Solution()
    res=obj.two_sum(nums,9)
    print("Result:",res)

if __name__=="__main__":
    main()