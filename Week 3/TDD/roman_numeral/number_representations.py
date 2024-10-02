def to_roman_numeral(number):
    # Check if the input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
     # Check for special cases
    if number == 0:
        # Handling 0 as per test case
        return None 
    if number < 1 or number > 3999:
        raise ValueError("Input must be an integer between 1 and 3999.")


    roman_numbers = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }
    
     
    result = ''

    for actual_num, letter in roman_numbers.items():
        while number >= actual_num:
            result += letter
            number -= actual_num 

    return result
