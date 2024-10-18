
def count_multiples(numbers):
    result = {i: 0 for i in range(1, 10)}  # Initialize dictionary with keys 1 to 9, all values set to 0
    
    # Iterate through each number in the input list
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:  # Check if the number is divisible by i
                result[i] += 1  # Increment the count for the corresponding i
    
    return result

if __name__ == "__main__":
    # Take input from the user and convert it to a list of integers
    numbers = list(map(int, input("Enter the numbers separated by commas: ").split(',')))
    
    # Get the count of multiples
    multiples_count = count_multiples(numbers)
    
    # Print the result
    print(multiples_count)
