from collections import Counter

def subsets(nums):
    def backtrack(start,current_list):
        result.append(current_list[:])
        for i in range(start,len(nums)):
            current_list.append(nums[i])
            backtrack(i+1,current_list)
            current_list.pop()
    result=[]
    backtrack(0,[])
    return result    

def main():
    nums=[45,23,89]
    res=subsets(nums)
    print("Subsets:",res)

if __name__=="__main__":
    main()