while True:
    x = int(input('Для начала игры введите 0: '))
    if x == 0:
        text = str(input('Введите текст на русском: '))
        symbol = str(input('Введите символ: '))
        punctuation = ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
        consonant = 'бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ' # согласные
        vowel = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ' # гласные
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
