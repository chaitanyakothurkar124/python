n = int(input("Enter your number: "))

for i in range(1, n):
    if(n%i) == 0:
        print("Your number is a not a prime number")
        break
else:
        print("your number is a prime number")