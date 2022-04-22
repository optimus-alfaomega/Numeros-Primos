def isPrime(num):
    if num > 1:
        if num % 2 != 0:
            return True
        else:
            return False
    
for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()