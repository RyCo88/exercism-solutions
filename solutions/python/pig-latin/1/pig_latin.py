def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    translated = []
    for word in words:
        letters = ''
        if word[:2] == 'xr' or word[:2] == 'yt':
            translated.append(word + 'ay')
        elif word[0] in vowels:
            translated.append(word + 'ay')
        elif word[0] == 'y':
            translated.append(word[1:] + 'yay')
        elif word[0] not in vowels and 'y' in word:
            i = 0
            while word[i] != 'y':
                if word[i] in vowels:
                    break                
                letters += word[i]
                i += 1
            translated.append(word[len(letters):] + letters + 'ay')
        elif word[0] not in vowels and 'qu' in word:
            i = 0
            while letters.endswith('qu') == False:
                letters += word[i]
                i += 1
            translated.append(word[len(letters):] + letters + 'ay')
        else:
            i = 0
            while word[i] not in vowels:
                letters += word[i]
                i += 1
            translated.append(word[len(letters):] + letters + 'ay')
    return ' '.join(translated)