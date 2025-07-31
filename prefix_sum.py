class Solution: 
    def subarray_sum(self,nums,queries,limit):
        #Finding the Prefix Sum first
        sum=0
        result=[]
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[len(prefix)-1])
        
        for a,b in queries:
            sum=prefix[b]-prefix[a]+nums[a]
            if sum>limit:
                result.append(False)
            else:
                result.append(True)
            print(sum)
        return result
        
        """
        Another Method
        for q in queries:
            diff=prefix[q[1]]-prefix[q[0]]
            sum=diff+nums[q[0]]
        sum=0
        """

def main():
    nums=[1, 6, 3, 2, 7, 2]
    #prsm=[1, 7,10,12,19,21]
    queries=[[0,3],[2,5],[2,4]]
    limit=13
    obj=Solution()
    res=obj.subarray_sum(nums,queries,limit)
    print("Result:",res)

if __name__=="__main__":
    main()