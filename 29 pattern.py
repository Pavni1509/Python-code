#Number of rows for pattern

print("\n")
print("Pattern 1")
rows=5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
    
print("\n")
print("Pattern 2")
rows=5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j,end="")
    print()

print("\n")
print("Pattern 3")
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end="")
    print()   

print("\n")
print("Pattern 4")
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
     print("*", end="")
    print()

print("\n")   
print("Pattern 5")
rows=5
for i in range(rows,0,-1):
    for j in range(rows,rows-i,-1):
     print(j,end="")
    print()

print("\n")
print("Pattern 6")
rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print(i,end="")
    print()

print("\n")
print("Pattern 7")
rows=5
for i in range(1, rows+1):
    for j in range(rows - i):
        print("", end="")
    for k in range(i):
            print("*",end="")
    print()

print("\n")
print("Pattern 8")
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ", end="")
    for k in range(2*i-1):
            print("*",end="")
    print()


print("This program is done by Pavni Suri-0221BCA030")
