def fizz_buzz(num):
  num = int(input("enter a number: "))
  if num%3==0 and num%5==0:
    return "FizzBuzz"
  elif num%5==0 and num%3!=0:
    return "Fizz"
  elif num%3==0 and num%5!=0:
    return "Buzz"
  else:
    return str(num)