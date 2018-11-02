while True:
    x = int(input('To start the game print 0: '))
    if x == 0:
        text = str(input('Please enter the text in Russian language: '))
        symbol = str(input('Please enter the symbol: '))
        punctuation = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
        consonant = 'бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'  # согласные
        vowel = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'  # гласные
        s = None
        a = []
        for w in text:
            if w in punctuation:
                s = w
            elif w in vowel:
                s = w + symbol + w.lower()
            if w in consonant:
                s = w
            a += s
        print("".join(a))
    if x != 0:
        break
