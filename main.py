#Write your code below this line 👇

def prime_checker(number):
  prime = 0
  for x in range(2, number):
    if number % x == 0:
      prime += 1
  if prime == 0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



