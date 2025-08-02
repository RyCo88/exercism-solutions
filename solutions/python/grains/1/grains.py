'''Find the number of grains on a given square
    number will be the number of square we're checking for the number of grains
    a Value Error will be raised if the number of the square is less than 1 or over 64 since a maximum of 64 sqares are available on a chessboard
    this is written as 2 to the power of (number - 1)'''
def square(number):
        if number > 64 or number < 1:
            raise ValueError("square must be between 1 and 64")
        else:
            return 2 ** (number - 1)


'''Find the total of all grains of wheat on a chessboard
    this is written as 2 to the power of 64 - 1 to account for each grain on each square'''
def total():
    return 2 ** 64 - 1