print('Create and Modify a List:'.upper())
l = [1, 2, 3, 4, 5] 
print("Original List: ", l)
l.append(6) 
print("Append: ", l)
l.insert(2, 2.5) 
print("Insert: ", l)
l.remove(4) 
print("Remove: ", l)

print('\nSlice and Access List Elements:'.upper())
l = ['a', 'b', 'c', 'd', 'e']
print("Original List: ", l) 
print("First element:", l[0])
print("Last element:", l[-1])
print("Sliced list:", l[1:len(l)-1])

print("This program is written by Pavni Suri-0221BCA030")
