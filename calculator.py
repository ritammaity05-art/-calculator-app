# Function to add two numbers
def add(x, y): return x + y

# Function to subtract
def subtract(x, y): return x - y

# Function to multiply
def multiply(x, y): return x * y

# Function to divide
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("--- Ritam's Python Calculator ---")
print("Choose Operation: 1.Add, 2.Subtract, 3.Multiply, 4.Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("First number dalo: "))
num2 = float(input("Second number dalo: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid Input!")