def recurse(n)
    if n<0:
      return n
    else:
      recurse(n-1)+recurse(n-2)


def main():
  n=5
  recurse(n)

if __name__==__main__:
  main()
