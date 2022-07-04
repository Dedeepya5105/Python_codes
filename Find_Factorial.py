# In this program we give an integer as an input and it prits the factorial of that number

f = 1
n = int(input("Enter a Number: "))

if n<0:
    print("Cannot be found")
elif n ==0:
    print("1")
else:
    for i in range(1,n+1):
        f = f*i
    print(f)
    

''' sample input 5
    sample output 120'''


