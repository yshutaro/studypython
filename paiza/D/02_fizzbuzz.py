def main():
  num = int(input().rstrip())
  for i in range(1, num + 1):
    if i % 15 == 0:
      print('Fizz Buzz')
    elif i % 3 == 0:
      print('Fizz')
    elif i % 5 == 0:
      print('Buzz')
    else:
      print(i)

if __name__ == '__main__': main()

