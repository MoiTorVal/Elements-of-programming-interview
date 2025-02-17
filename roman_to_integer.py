def romanToInt(s: str) -> int:
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    num = 0
    i = 0

    while i < len(s):
    # Check if the current character and the next character form a valid pair
        if i + 1 < len(s) and s[i] + s[i+1] in roman_num:
            num += roman_num[s[i] + s[i+1]]
            i += 2  # Skip the next character
        else:
            num += roman_num[s[i]]
            i += 1  # Move to the next character

    return num

                
print(romanToInt('CMXCIVI'))
