# name = " ---My name is @@ sujata pathak 123__"
# *? My name is sujata pathak
# newName=name.strip(" -123_")
# newName1=newName.replace(" @@","")
# print(newName1)
'''
title() ->makes the initial letter capital
split()-> breakes the words to make it different
'''

# name="sujata pathak"
# capatalized = name.title()
# print(capatalized)

# first_name , last_name = capatalized.split()
# print(first_name)
# print(last_name)
# !name = "sangam,x,puri"
# first_name ,middle_name, last_name =name.split(",")
# print(first_name)
# print(middle_name)
# print(last_name)

#?Task 1 Firoj Karki with K capital
# name = "  __--firoj ##&& karki 123 @@"
# name1 = name.strip(" _- 123@")
# name2 = name1.replace(" ##&& "," ")
# name3 = name2.title()
# first_name , last_name= name3.split()
# print(first_name)
# print(last_name)

#?Task 2 output: Firoj karki with k small 
name = "  __--firoj ##&& karki 123 @@"
name1 = name.strip(" _-123@")
name2 = name1.replace(" ##&& "," ")
name3 = name2
first_name , last_name= name3.split()
print(first_name.title())
print(last_name)