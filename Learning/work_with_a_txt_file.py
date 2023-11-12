
# read a file
employee_file = open("employees.txt", "r") # r = read; w = write; r+ = read and write; a = append

for employee in employee_file.readlines():
    print(employee)

#print(employee_file.readlines()) # transforma fisierul txt in array

employee_file.close()

# write a file

employee_file = open("employees.txt", "a") # a adauga la un fisier existent # r = scrie un noudocument
employee_file.write("\nKelly - Customer Service")





