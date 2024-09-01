proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
comma = ','
space = ' '
semicolon = ';'


if comma in proto_list1: 
    print("Commas are the delimiter in list 1")
elif space in proto_list1:
    print("Spaces are the delimiter in list 1")
elif semicolon in proto_list1:
    print("semicolons are the delimiter in list 1")


if comma in proto_list2: 
    print("Commas are the delimiter in list 2")
elif space in proto_list2:
    print("Spaces are the delimiter in list 2")
elif semicolon in proto_list2:
    print("semicolons are the delimiter in list 2")


if comma in proto_list3: 
    print("Commas are the delimiter in list 3")
elif space in proto_list3:
    print("Spaces are the delimiter in list 3")
elif semicolon in proto_list3:
    print("semicolons are the delimiter in list 3")


if comma in proto_list4: 
    print("Commas are the delimiter in list 4")
elif space in proto_list4:
    print("Spaces are the delimiter in list 4")
elif semicolon in proto_list4:
    print("semicolons are the delimiter in list 4")


  

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
proto_list1 = (proto_list1.split(","))
proto_list1.reverse()
str(proto_list1)
proto_list1 = ",".join(proto_list1)
print(proto_list1)



# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
proto_list2 = (proto_list2.split(";"))
proto_list2.sort()
str(proto_list2)
proto_list2 = ",".join(proto_list2)
print(proto_list2)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
proto_list3 = (proto_list3.split(" "))
str(proto_list3)
proto_list3 = " ".join(sorted(proto_list3, reverse= True))
print(proto_list3)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
proto_list4 = (proto_list4.split(", "))
proto_list4.reverse()
str(proto_list4)
proto_list4 = ",".join(proto_list4)
print(proto_list4)