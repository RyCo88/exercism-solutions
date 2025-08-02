'''To find if arg:number == armstrong number
    We make number a list(numbers) of its own digits as individual integers
    Since an Armstrong number is "the sum of its own digits each raised to the power of the number of digits" we assign variable x to the length of numbers to be the representation of the power we will raise each individual digit to
    We create another variable armposs and assign it to 0
    We then take each indivudual digit ** x and add that result to armposs
    we then check to see if armposs is equal to our original number
    if it is, it is an Armstrong number'''
def is_armstrong_number(number):
    numbers = [int(digit) for digit in str(number)]
    x = len(numbers)
    armposs = 0
    for i in numbers:
        armposs += i ** x
    return armposs == number
