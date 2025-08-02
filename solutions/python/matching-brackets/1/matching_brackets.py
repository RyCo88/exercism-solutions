def is_paired(input_string):
    bracket_list = []
    bracket_pair = {')' : '(', ']' : '[', '}' : '{'}
    for char in input_string:
        if char in bracket_pair.values():
            bracket_list.append(char)
        elif char in bracket_pair.keys():
            if bracket_list == [] or bracket_list.pop() != bracket_pair[char]:
                return False
    return bracket_list == []