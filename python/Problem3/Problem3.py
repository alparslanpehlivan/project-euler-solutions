K=600851475143
L=2

while L<K:
    if K%L == 0:
        num = L

        # take input from the user
        # num = int(input("Enter a number: "))

        # prime numbers are greater than 1
        if num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                num2=num

        # if input number is less than
        # or equal to 1, it is not prime
        else:
            print(num, "is not a prime number")

    L+=1
print(num2, "is a prime number")
