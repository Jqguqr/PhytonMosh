def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FIZZBUZZ"
    elif input % 5 == 0:
        return "BUZZ"
    elif input % 3 == 0:
        return "FIZZ"
    else:
        return input


print(fizz_buzz(7))
