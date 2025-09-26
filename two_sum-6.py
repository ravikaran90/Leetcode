class Solution:
    def two_sum(self,nums,target):
        diction={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in diction:
                return [diction[compl],i]
            diction[nums[i]]=i

def main():
    nums=[2,7,10,14,16]
    obj=Solution()
    res=obj.two_sum(nums,16)
    print("Result:",res)

if __name__=="__main__":
    main()