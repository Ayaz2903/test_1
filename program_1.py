class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()  # Convert the operation to lowercase for easier comparison

    def calculate(self):
        if self.operation == 'add':
            return self.add()
        elif self.operation == 'subtract':
            return self.subtract()
        elif self.operation == 'multiply':
            return self.multiply()
        elif self.operation == 'divide':
            return self.divide()
        else:
            return "Invalid operation"

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error! Division by zero."
        return self.a / self.b


# Example usage
if __name__ == "__main__":
    # Take inputs from the user
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    # Create a Calculator object
    calc = Calculator(a, b, operation)

    # Perform the calculation and display the result
    result = calc.calculate()
    print(f"Result: {result}")
