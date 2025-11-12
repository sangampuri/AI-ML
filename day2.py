# *? --------------------------------------------Datacleaning---------------------------------------------------------------------------
'''
lstrip() ->  Removes spaces or anyother characters from left side
rstrip() -> Removes spaces or anyother characters from right side
strip()
replace() -> Replaces something with other thing from anywhere
'''
#name = "  ---My ---Sister's name is Sujata 123__ " -> present data
#name ="My sister's name is Sujata"

# *TODO name = "  Samriddha"
# new_name = name.lstrip()
# print(new_name)

# name = "-- Sangam Puri__"
# new_name = name.lstrip("-- ").rstrip("__")
# print(new_name)

# name = "  ---My ---Sister's name is Sujata 123__ "
# new_name = name.lstrip("  ---").rstrip(" 123__")
# finalName = new_name.replace(" ---"," ")
# print(finalName)

# *!  doing  above thing using strip
# name = "  ---My ---Sister's name is Sujata 123__"
# newName = name.strip("       - 123_")
# finalName = newName.replace(" ---"," ")
# print(finalName)

name1 = "--- My name ___ is Ram 123 karki --"
newName = name1.strip("- ")
finalName = newName.replace(" ___","")
final_Name = finalName.replace("123 ","")
print(final_Name)

#checking