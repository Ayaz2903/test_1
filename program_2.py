def generate_odd_numbers(a: int):
    result = []
    for i in range(a):
        result.append(2 * i + 1)  # Generate the ith odd number
    return result


# Example usage
if __name__ == "__main__":
    # Take input from the user
    a = int(input("Enter a number (a): "))
    
    # Generate and print the series of odd numbers
    result = generate_odd_numbers(a)
    print(f"Output: {', '.join(map(str, result))}")
