print('Creating and Modifying:'.upper())
dic = {'name': 'PS', 'age': 20}
dic['age'] = 21
dic['city'] = 'New Delhi'
print(dic)

print('\nAccessing and Removing Elements:'.upper())
print('Name:',dic.get('name'))
dic.pop('name')
print(dic)

print('\nIterating Through Dictionary Items:'.upper())
for key, value in dic.items():
    print(f"{key}: {value}")

print("This program is written by Pavni Suri-0221BCA030")
