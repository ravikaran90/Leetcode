class Solution:
    def two_sum(self,nums,target):
        diction={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in diction:
                return [i,diction[compl]]
            diction[nums[i]]=i
        
def main():
    nums=[1,2,4,5,7,8,11,15]
    obj=Solution()
    res=obj.two_sum(nums,10)
    print("Result:",res)

if __name__=="__main__":
    main()