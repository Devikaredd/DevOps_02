def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    str_num = str(num)
    num_digits = len(str_num)
    
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    
    # Check if the sum is equal to the original number
    return sum_of_powers == num

# Input from the user
try:
    number = int(input("Enter a number: "))
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")
