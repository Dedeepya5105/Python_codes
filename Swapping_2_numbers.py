#Swapping 2 numbers

print("Before Swapping")
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

a = a + b
b = a - b
a = a - b

print("After Swapping")
print(a)
print(b)
