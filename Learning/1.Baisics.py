from math import * # see line 104

# Printing in the console with Python
print("----Printing in the console with Python----")
print("    /|") # executes the lines of code in order inserted
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print ("---------------------------------------------------------------------------------------------------------------------")
# Variables in Python
print("----Variables in Python----")
character_name = "George" # by changing the variable name between " " (quote marks) we change in all the program below that information
character_age = "70" # this type of data in quote marks (" ") is used to define a String
# a String is (plain text) an array of bytes representing Unicode characters
print("There once was a man named " + character_name + ", he was " + character_age + " years old.")
character_name = "Mike" # here I've updated the variable name at the middle of
print("He really liked the name " + character_name + ", but didn't liked being " + character_age + ".")
is_male = True # boolean
number = 54.5464 # you can add any kind of numbers in Python - int, float, double, with negative value, etc.
print("---------------------------------------------------------------------------------------------------------------------")
# String and Functions using Strings
print("----String and Functions using Strings----")
print("Self studying mind academy") # to add a qoutation mark we use it by adding a \ (back slash)
phrase = "Self studying mind academy"
print("---------------------------------------------------------------------------------------------------------------------")
print(phrase) # here we print the value of the String by calling the variable where we defined the String
print("---- concatenation ----")
print(phrase + " is cool") # this is a concatenation => adding text together
print("---- convert to lower ----")
print(phrase.lower()) # by calling lower we convert the String in the variable as lower case characters
print("---- convert to upper ----")
print(phrase.upper()) # converts the entire String to upper case characters
print("---- check if isupper ----")
print(phrase.isupper()) # this will return if the characters in the String are upper (True or False)
print("---- convert to upper and check if is upper ----")
print(phrase.upper().isupper()) # this line of code will convert the entire String variable in upper case and will return the value True as is upper
print("----Working with String Variable to return it's length, \n a value to a specific index, etc----")
print("---- check the length of the variable ----")
print(len(phrase)) # here we check how many characters are in the String (how long is the phrase variable in character value)
# index allways starts counted from 0
print("---- return the value from the variable at a certain index ----")
print(phrase[0]) # this line of code will return the value from variable phrase at the position 0 (zero)
print("---- Check the inserted value and return the index position in the variable ----")
print(phrase.index("S")) # we give a parameter (value to our index to search for in the String variable)
# the value of capital S is stored at the index 0 in the variable phrase
print("---- return the index value of the \"m\" ----")
print(phrase.index("m")) # this will return the value in index where "m" is located in the String variable
print("---- return the index value from a set of characters ----")
print(phrase.index("acad")) # we can use parts of a word or words to find the index where starts in the String
# if we insert a character which is not located in the String variable the program will throw an ValueError: sustracting not found
print("----  ----")
print(phrase.replace("Self studying", "Elephant")) # so, we can replace a value in the String variable
print("---------------------------------------------------------------------------------------------------------------------")
# Working with Numbers in Python
print("----Working with numbers----")
print("---- float negativ number ----")
print(-2.0987) # negative numbers
print("---- addition ----")
print(3 + 4.5) # +
print("---- multiplication ----")
print(3 * 4.5) # *
print("---- division ----")
print(3 / 4.5) # /
print("---- subtraction ----")
print(3 - 4.5) # -
print("----the first number is rised to the power of the second number ----")
print(9**2) # this is 9 to the power of 2 . can be written as well as: print (pow(9 , 2))
print("---------------------------------------------------------------------------------------------------------------------")
print("---- changing the order of accountin in an ecuation ----")
print(3 * (4 + 4.5)) # we change the order of the ecuation by adding ()
print("---- modulo ----")
print(10 % 3) # 10 mod 3 = 1 as 3*3 = 9 and so the difference to 10 is 1 and this difference is the monulo
print("---------------------------------------------------------------------------------------------------------------------")
# we can use variables to store values for math ecuations too
print("---- we inserted our variable value ----")
my_num = -5
print("---- and we print the variable value ----")
print(my_num)
print("---- We convert a number to a String ----")
print(str(my_num)) # so we can convert a number to a String, this is handy when we want to convert numbers near a String
print("---- We convert a number to a String and we concatenat it with other inserted String value ----")
print(str(my_num) + " is my favorite number for now") # this is a concatenation of my_num with the String added value
# print (my_num + " is my favorite number for now") # Python will not allow this and so will return an error as:
# TypeError> unsupported operand type(s) for +: 'int' and 'string'
print("---------------------------------------------------------------------------------------------------------------------")
# Math functions
print("----Math functions----")
print("---- returnes the absolute value of a number ----")
print(abs(my_num)) # abs (absolute value of a number) # in this case of negative five the abs is five
print("---- the first number is raised to the power of the second number ----")
print(pow(3 , 2)) # pow ( 3 raised to the power of 2)
print("---- !!!I have no clue what this will return. Neither as it's works!!! ----")
print(9^2) # What is `^` in `x^u` , it only allows `int` for `u` . ex: 9^int(2) = 11
print("---- return the largest number between ----")
print(max(4 , 6)) # this will return the largest number between the two, here 6
print("---- return the smallest number between ----")
print(min (4, 6)) # this will return the smallest number between the two, here 4
print("---- down round numbers from 4 ----")
print(round(3.2)) # this will round the 3.2 to 3.
print("---- up round numbers from 5 ----")
print(round(3.7)) # this will round the 3.2 to 4.
print("---------------------------------------------------------------------------------------------------------------------")
#to import a library in Python we make it as: from math import *
print("---- returns the integer from a float ----")
print(floor(3.7)) # the result is 3. will chop off anything after to return an int.
print("---- returns the square roots (radical) from the inserted number ----")
print(sqrt(36)) # this will return the square root of a number. to 36 is 6