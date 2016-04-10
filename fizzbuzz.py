num = raw_input("Select a number between 1 and 100:")

# fix: wenn nummer nicht range 1-100 is

for num in range(1, 101):
    if (num % 3) == 0 and (num % 5) == 0:
        message = ("fizzbuzz")
    elif num % 3 == 0:
        message = ("fizz")
    elif num % 5 == 0:
        message = ("buzz")
    #if num < 1 and num > 101:
        #message = ("Your number was not in the expected range. Select a number between 1 and 100:")
    else:
        message = num
    print message
