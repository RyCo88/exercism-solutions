def is_pangram(sentence):
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set([x.lower() for x in sentence if x.isalpha()])
    return alpha == sentence_set
