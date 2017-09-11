from collections import OrderedDict

def main():
  slist = input().rstrip().split(' ')
  dict = OrderedDict()
  for str in slist:
    dict[str] = slist.count(str)

  for k,v in dict.items():
    print(k,end=' ')
    print(v)

if __name__ == '__main__': main()
