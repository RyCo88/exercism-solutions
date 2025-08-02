def is_isogram(string):
    string_list = [x.lower() for x in string if x.isalpha()]
    string_set = set([x.lower() for x in string if x.isalpha()])
    return len(string_list) == len(string_set)
