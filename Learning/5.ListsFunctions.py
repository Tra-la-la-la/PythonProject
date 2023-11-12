
luckey_numbers = [4, -5, 53, 8.2, 165, False, 16, -23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Jim", "Oscar", "Toby"]

print("---- will sort the list in an alphabetical/numerical oder ----")
print("---- String list ----") # boolean is not supported with String values to be sort, revers, etc.
friends.sort() # we can only use the sort function before extended with int, float, boolean
print(friends)
print("---- Numerical list ----") # boolean is supported with numerical values
luckey_numbers.sort()
print(luckey_numbers)
print("---- We revers a list order ----")
luckey_numbers.reverse() # this litteraly revers the order of the list
print(luckey_numbers)

print("---- we make a copy of the list ----")
friends2 = friends.copy()
print(friends2)

print("---- we extend the list by the luckey_numbers variable list ----")
# extend function = will alow you to take a list and append another one to it
friends.extend(luckey_numbers)
print("---- append (we add another item to our list)----")
friends.append("Creed") # we append (add) another item to our frients list
print("---- we insert at the index 1 a specific value ----")
friends.insert(1, "Kelly") # we add at index position 1 a value named "Kelly" and all the rest are moved up +1 index value
print("---- we remove a specific value ----")
friends.remove("Jim") # will remove on specific value from the list

print("---- pop - will pop off the last value in the list ----")
friends.pop() # will remove the last element in the list

print("---- search for a specific value in the list ----")
print(friends.index("Oscar")) # will return the index of value where Oscar is saved

print("---- Count how many time a value is repeated ----")
print(friends.count("Jim"))

print("---- commented ValueError: 'Mike' is not in the list ----")
#print(friends.index("Mike"))
print("---- clear all the data in a list ----")
friends2.clear() # will clear the list

print(friends)