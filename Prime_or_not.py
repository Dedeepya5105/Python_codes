# Prime Number

n = int(input("Enter the Number: "))

for i in range(2,n):
    if n % i == 0:
        print("N is not Prime")
        break
    else:
        print("N is Prime")
        
        
