def twosum(nums,target):
    dict={}
    for i in range(len(nums)):
        compl=target-nums[i]
        if compl in dict:
            return [dict[compl],i]
        dict[nums[i]]=i

def main():
    nums=[2,7,11,15]
    target=9
    indices=twosum(nums,target)
    print("Indices:",indices)

if __name__=="__main__":
    main()