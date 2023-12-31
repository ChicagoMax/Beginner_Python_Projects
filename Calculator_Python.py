#define the functions needed, add, sub, mul,div
#print options to the user 
#while loop to continue


def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def subtract(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
     
def multiply(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))
     
def divide(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

print("A. Add")
print('B. Subtract')
print("C. Multipy")
print("D. Divide")
print('E. Exit')

choice = input("What would you like to do? ")

if choice == ('a') or choice ==('A'):
    print("Addition")
    a = int(input("what is your first number? "))
    b = int(input("What is your second number? "))
    add(a,b)
    
elif choice == ('b') or choice == ('B'):
    print("B: subtraction")
    a = int(input("what is your first number? "))
    b = int(input("What is your second number? "))
    subtract(a,b)

elif choice == ('c') or choice == ('C'):
    print("C: Multiply")
    a = int(input("what is your first number? "))
    b = int(input("What is your second number? "))
    multiply(a,b)

elif choice == ('d') or choice == ('D'):
    print("D: divide")
    a = int(input("what is your first number? "))
    b = int(input("What is your second number? "))
    divide(a,b)


