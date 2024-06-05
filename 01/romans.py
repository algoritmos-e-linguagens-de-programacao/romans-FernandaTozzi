def int_to_roman(num):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    result = ''
    for value, numeral in roman_numerals.items():
        while num >= value:
            result += numeral
            num -= value
    return result

def roman_to_int(s):
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    result = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman_numerals:
            result += roman_numerals[s[i:i+2]]
            i += 2
        else:
            result += roman_numerals[s[i]]
            i += 1
    return result

# def main():
#     choice = input("Escolha uma opção:\n1. Converter número inteiro para romano\n2. Converter número romano para inteiro\n")
    
#     if choice == '1':
#         num = int(input("Digite um número inteiro: "))
#         print("Número romano correspondente:", int_to_roman(num))
#     elif choice == '2':
#         roman_num = input("Digite um número romano: ")
#         print("Número inteiro correspondente:", roman_to_int(roman_num))
#     else:
#         print("Opção inválida. Escolha 1 ou 2.")

# if __name__ == "__main__":
#     main()
