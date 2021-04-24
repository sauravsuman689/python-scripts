#Take a number input from a user to check whether it's prime or not..!
num = input("Enter a Integer number to check if it's prime or not = ")

mark = False

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            # If the number is divisble then it's not prime number and break the loop.
            mark = True
            break

#If the check mark is True then it's not a prime number else it's a prime number
if mark:
    print("The Input number {} is a not a prime number".format(num))
else:
    print("The Input number {} is a prime number".format(num))

