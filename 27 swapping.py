#WAP to swap two numbers
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))

#using 3rd variable
temp=a
a=b
b=temp
print(f'Numbers after swapping: {a}, {b}')

#without using 3rd variable
a=int(input("\nEnter First Number: "))
b=int(input("Enter Second Number: "))
a=a+b
b=a-b
a=a-b
print(f'Numbers after swapping: {a}, {b}')

print("This program is done by Pavni Suri-0221BCA030")