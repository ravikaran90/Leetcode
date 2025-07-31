class Solution: 
    def highest_altitude(self,gain):
        prefix=[gain[0]]
        for i in range(1,len(gain)):
            prefix.append(gain[i]+prefix[len(prefix)-1])
        if max(prefix)<0:
            return 0
        else:
            return max(prefix)

def main():
    gain=[-4,-3,-2,-1,4,3,2]
    obj=Solution()
    res=obj.highest_altitude(gain)
    print("Result:",res)

if __name__=="__main__":
    main()