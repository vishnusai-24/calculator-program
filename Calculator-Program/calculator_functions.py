def multiply(numbers):
    """
    Function to multiply a list of numbers.
    
    Args:
        numbers (list): List of numbers to be multiplied.
        
    Returns:
        int: The product of the numbers.
    """
    result = 1
    for num in numbers:
        result *= num
    return result

def subtract(numbers):
    """
    Function to subtract two numbers.
    
    Args:
        numbers (list): List of two numbers for subtraction.
        
    Returns:
        int: The result of the subtraction.
    """
    return numbers[0] - numbers[1]

def divide(numbers):
    """
    Function to divide two numbers.
    
    Args:
        numbers (list): List of two numbers for division.
        
    Returns:
        float: The result of the division.
    """
    return numbers[0] / numbers[1]

def add(numbers):
    """
    Function to add a list of numbers.
    
    Args:
        numbers (list): List of numbers to be added.
        
    Returns:
        int: The sum of the numbers.
    """
    return sum(numbers)
