from collections import Counter

class Solution:
    def subsets(self,root):
        def backtrack(start,current_list):
            result.append(current_list[:])
            for i in range(start,len(nums):
                
        result=[]
        backtrack(0,[])
        return result


def main():
    nums=[5,7,9]
    obj=Solution()
    res=obj.subsets(nums)
    print("Result:",res)

if __name__=="__main__":
    main()