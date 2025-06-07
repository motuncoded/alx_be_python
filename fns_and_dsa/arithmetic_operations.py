def perform_operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation == "add":
        print("The result is", num1 + num2);
    elif operation == "subtract":
        print("The result is", num1 - num2);
    elif operation == "multiply":
        print("The result is", num1 * num2);
    elif operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("The result is", num1 / num2);  
        
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    perform_operation(num1, num2, operation)