class Solution:
    def twosum(self, arr, target):
        sum=0
        for i in range(len(arr)):
            left=0
            right=len(arr)-1
            sum=arr[left]+arr[right]
            if sum==target:
                return [left,right]
            elif sum<target:
                left+=1
            elif sum>target:
                right+=1
        return None

def main():
    arr=[3,5,8,10,13,16,19,21,25]
    obj=Solution()
    res=obj.twosum(arr,32)
    print("Result:",res)

if __name__=="__main__":
    main()




