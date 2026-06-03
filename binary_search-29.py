def binary_search(nums,target):
  l=0
  r=len(nums)-1
  while l<r:
    mid=((l+r))/2
    if target<mid:
      r=mid-1
    elif target>mid:
      l=mid+1
    l+=1
    r-=1
  return mid

def main():
  nums=[5,45,47,65,67,78,88,89,92,95]
  res=binary_search(nums)
  print("Sorted:",res)

if __name__==__main__:
  main()
