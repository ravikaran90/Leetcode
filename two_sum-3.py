class Solution:
    def two_sum(self,nums,target):
        diction={}
        for i in range(len(nums)):
            compl=abs(nums[i]-target)
            if compl in diction:
                return [diction[compl],i]
            diction[nums[i]]=i

def main():
    nums=[2,4,6,8,12,15,16]
    obj=Solution()
    res=obj.two_sum(nums,28)
    print("Indexes:",res)

if __name__=="__main__":
    main()