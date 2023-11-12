name = input ("Enter your name ") # we stored a inpute value in this variable called name
age = input ("Enter your age ")
print ("Hello " + name + " ! You are " + age)
print ("---------------------------------------------------------------------------------------------------------------------")
# We create a calucaltor with input from the user
print ("---- We create a calucaltor with input from the user ----")
num1 = input ("Enter a number: ") # We insert the data as a String, so this will create a concatenation
num2 = input ("Enter another number: ") # We insert the value as a String, so this will create a concatenation
print("---- inserteed value concatenation ----")
result = num1 + num2 # this is a concatenation
print("---- inserted value as a float to be accounted +----")
result = float(num1) + float(num2) # this will convert the numbers to integers using "int" or to float using "float" and so will be accounted
print (result)
