class Solution:
    def contains_duplicate(self,nums):
        duplicate=[]
        for val in nums:
            if val in duplicate:
                return True
            duplicate.append(val)
        return False

def main():
    nums=[1,2,3]
    obj=Solution()
    res=obj.contains_duplicate(nums)
    print("Result:",res)

if __name__=="__main__":
    main()