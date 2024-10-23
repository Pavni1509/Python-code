#Iterator
a = 'Pavni Suri'

print('Custom Iterator:')
result = ' '.join(char for char in a)
print(result)

print('\nCustom Iterator with yield:')
def char_gen(s):
    for char in s:
        yield char
for char in char_gen(a):
    print(char, end=' ')

print('\n\nBuilt-in Iterator:')
for char in iter(a):
    print(char, end=' ')
    
print("This program is written by Pavni Suri-0221BCA030")
