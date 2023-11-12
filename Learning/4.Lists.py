
# lists in Python always use: [ ]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby", 2 , False] # sotre a bunch of values in this list
# we can store Stings, numbers, boolean = python is just fine
# each value inserted in a list have an index. Always the index starts from 0.
print("---- print the friends list ----")
print (friends)
print("---- return an index from a specific value ----")
#to return an index from a specific value from the list we call it as:
print (friends[2]) # will return index 2 which is: Jim
print("---- negative index returnes the from the back of the list ----")
print (friends[-1]) # if we use negative indexing will start from the back of the list
print("---- call from a specific element stored at an index we choose ----")
# if we want to call all the elements except the first one we call it as:
print (friends[1:]) # 1: this will call all the elements starting from index value one and above
print("---- to call elements between some inserted value ----")
print (friends[1:3]) # 1: this will call all the elements starting from index value 1 unti 3
print("---- to modify/change a value from a certain position ----")
#if we want to modify the value from a certain positon:
friends[1] = "Mike"
print(friends[1]) # we changed "Karen" with "Mike"
