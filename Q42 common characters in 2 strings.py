def common_characters(s1, s2):
    return ','.join(set(s1) & set(s2))
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Common characters:", common_characters(s1, s2))
print("This program is done by Pavni Suri-0221BCA030")