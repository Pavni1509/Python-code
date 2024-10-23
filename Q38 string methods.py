text = "Hello World!"
#Changing case
lower_txt = text.lower()
upper_txt = text.upper()
title = text.title()
print(lower_txt)
print(upper_txt)
print(title)
#Removing white space
str_txt = text.strip()
words = str_txt.strip()
joined = "-".join(words)
print(str_txt)
print(words)
print(joined)
#Replace and finding
rep = str_txt.replace("World","Python")
index = str_txt.find("World")
count = str_txt.count("o")
print(rep)
print(index)
print(count)
print("This program is done by Pavni Suri-0221BCA030")
