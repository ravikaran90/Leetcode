def binary_search(n,target):
  l=0
  r=len(n)-1
  while l<r:
    mid=(l+r)//2
    if target>mid:
      l=mid+1
    elif target<mid:
      r=mid-1
    l+=1
    r-=1

def main():
  n=[6,8,78,90,35,32]
  res= binary_search(n,78)
  print("Result:",res)

if __name__==__main__:
  main()
