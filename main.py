from time import sleep

def intro():
    print("""
    
    ██████╗░███████╗░█████╗░██████╗░░█████╗░██████╗░██╗██╗░░░░░██╗████████╗██╗░░░██╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██║░░░░░██║╚══██╔══╝╚██╗░██╔╝
    ██████╔╝█████╗░░███████║██║░░██║███████║██████╦╝██║██║░░░░░██║░░░██║░░░░╚████╔╝░
    ██╔══██╗██╔══╝░░██╔══██║██║░░██║██╔══██║██╔══██╗██║██║░░░░░██║░░░██║░░░░░╚██╔╝░░
    ██║░░██║███████╗██║░░██║██████╔╝██║░░██║██████╦╝██║███████╗██║░░░██║░░░░░░██║░░░
    ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
    """)
intro()

try:
    text = input("\n\tƬΣXƬ: ")

    letters = 0
    words = 0
    sentences = 0
    count = 0

    for l in text:
        count += 1
    for i in range(count):
        # Counts the letters inside string
        if (ord(text[i]) >= 65 and ord(text[i]) <= 122):
            letters += 1

        # Find the number of spaces inside string
        elif (ord(text[i]) == 32 and (ord(text[i - 1]) != 33 and ord(text[i - 1]) != 46 and ord(text[i - 1]) != 63)):
            words += 1

        # Finds sentences by adding number of punctuation
        elif (ord(text[i]) == 33 or ord(text[i]) == 46 or ord(text[i]) == 63):
            sentences += 1
            words += 1

    L = letters * 100 / words
    S = sentences * 100 / words
    # Using the formula, the Coleman-Liau index is calculated
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if (index < 1):
        print('\n\tΛПΛLYZIПG ƬΣXƬ...')
        sleep(1)
        print('\n\t' + '-' * 15)
        print('\tBΣFӨЯΣ GЯΛDΣ 1')
        print('\t' + '-' * 15)
        input('\tPЯΣSS [ΣПƬΣR] ƬӨ ΣXIƬ')
    elif (index >= 16):
        print('\n\tΛПΛLYZIПG ƬΣXƬ...')
        sleep(1)
        print('\n\t' + '-' * 15)
        print("\tGЯΛDΣ 16+")
        print('\t' + '-' * 15)
        input('\tPЯΣSS [ΣПƬΣR] ƬӨ ΣXIƬ')
    else:
        print('\n\tΛПΛLYZIПG ƬΣXƬ...')
        sleep(1)
        print('\n\t' + '-' * 15)
        print(f"\tGЯΛDΣ {index}")
        print('\t' + '-' * 15)
        input('\tPЯΣSS [ΣПƬΣR] ƬӨ ΣXIƬ')
except Exception as e:
    print('\n\t' + '-' * 15)
    print('     !! ' + str(e) + ' !!')
    print('\t' + '-' * 15)
    input('\tPЯΣSS [ΣПƬΣR] ƬӨ ΣXIƬ')
