def rotate(text, key):
    alphalower = 'abcdefghijklmnopqrstuvwxyz'
    alphaupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipherlower = alphalower[key:] + alphalower[:key + 1]
    cipherupper = alphaupper[key:] + alphaupper[:key + 1]
    phrase = ''
    for i in text:
        if i.isalpha():
            if i in alphalower:
                phrase += cipherlower[alphalower.index(i)]
            else:
                phrase += cipherupper[alphaupper.index(i)]
        else:
            phrase += i
    return phrase