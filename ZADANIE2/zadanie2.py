ARABIC_TO_ROMAN = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

ROMAN_TO_ARABIC = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

print(ROMAN_TO_ARABIC)

def rzymskie_na_arabskie(rzymskie):
    if not isinstance(rzymskie, str):
        raise ValueError("Rzymska liczba musi być stringiem")
    
    if not all(c in ROMAN_TO_ARABIC for c in rzymskie):
        raise ValueError("Nieprawidłowe symbole rzymskie")
    
    wartosc = 0
    prev_value = 0
    for char in reversed(rzymskie):
        value = ROMAN_TO_ARABIC[char]

        if value < prev_value:
            wartosc -= value
        else:
            wartosc += value
        prev_value = value

    if wartosc < 1 or wartosc > 3999:
        raise ValueError("Liczba rzymska jest poza zakresem 1-3999")

    try:
        expected_value = arabskie_na_rzymskie(wartosc)
        if expected_value != rzymskie:
            raise ValueError("Nieprawidłowa konwersja")
    except ValueError:
        raise ValueError("Nieprawidłowa konwersja")

    return wartosc

def arabskie_na_rzymskie(arabskie):
    if not isinstance(arabskie, int):
        raise ValueError("Liczba arabska musi być liczbą całkowitą")
    
    if arabskie < 1 or arabskie > 3999:
        raise ValueError("Liczba arabska jest poza zakresem 1-3999")
    
    roman_numerals = ""

    for roman_value, roman_symbol in ARABIC_TO_ROMAN.items():
        while arabskie >= roman_value:
            roman_numerals += roman_symbol
            arabskie -= roman_value

    return roman_numerals

if __name__ == '__main__':
    try:
        rzymska = "IV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        
    except ValueError as e:
        print(e)
