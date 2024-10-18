# def count_multiples(numbers):
#     result = {i: 0 for i in range(1, 10)}  # Initialize dictionary with keys 1 to 9, all values set to 0
    
#     # Iterate through each number in the input list
#     for num in numbers:
#         for i in range(1, 10):
#             if num % i == 0:  # Check if the number is divisible by i
#                 result[i] += 1  # Increment the count for the corresponding i
    
#     return result

# # Example usage
# if __name__ == "__main__":
#     # Given input list
#     numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    
#     # Get the count of multiples
#     multiples_count = count_multiples(numbers)
    
#     # Print the result
#     print(multiples_count)

