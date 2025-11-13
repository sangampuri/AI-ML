# name = " ---My name is @@ sujata pathak 123__"
# *? My name is sujata pathak
# newName=name.strip(" -123_")
# newName1=newName.replace(" @@","")
# print(newName1)
'''
title() ->makes the initial letter capital
split()-> breakes the words to make it different
'''

name="sujata pathak"
capatalized = name.title()
print(capatalized)

first_name , last_name = capatalized.split()
print(first_name)
print(last_name)