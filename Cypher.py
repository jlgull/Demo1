# demo.py file from Learn PyCharm
message = 'GIEWIVrGMTLIVrHIQS'  # Encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQUSTUVWXYZ'
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
    print('Hacking key $%s: %s' % (key, translated))