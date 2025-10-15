import collections

class Solution:
    def valid_anagram(self,s,t):
        if collections.Counter(s)==collections.Counter(t):
            return True
        else:
            return False
        
def main():
    s="racecar"
    t="carrace"
    obj=Solution()
    res=obj.valid_anagram(s,t)
    print("Result:",res)

if __name__=="__main__":
    main()