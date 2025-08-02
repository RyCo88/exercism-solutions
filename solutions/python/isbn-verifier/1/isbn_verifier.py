def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    total = 0
    for i in range(10):
        if isbn[i].isdigit():
            total += int(isbn[i]) * (10-i)
        elif i == 9 and isbn[i] == 'X':
            total += 10
        else:
            return False
    return total % 11 == 0