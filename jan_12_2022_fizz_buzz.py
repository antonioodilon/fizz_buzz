import sys


# Try to use list comprehensions and expression comprehensions here!


def fizzbuzz():
    # global b
    _ = input("Let's play Fizz Buzz! Press any key to continue...")
    a = 0
    b = 0
    while True:
        a = int(input("First type in the first number in our range: "))
        # if a != int:
        if not isinstance(a, int):
            print("I am sorry, this is an invalid number. Please type in a "
                  "valid one")
            continue
        else:
            input("Ok, let's continue")
            pass
        b = int(input("Now type in the last number in our range: "))
        if b < a:
            print("The last number cannot be smaller than the first one.")
            continue
        if not isinstance(b, int):
            print("I am sorry, this is an invalid number. Please type in a "
                  "valid one")
            continue
        else:
            input("Ok, let's continue")
            break
            # pass
    # try:
    #     a = int(input("First type in the first number in our range: "))
    # except:
    #     print("I am sorry, this is an invalid number. Please type in a "
    #             "valid one")
    #     sys.exit()
    # try:
    #     b = int(input("Now type in the last number in our range: "))
    #     if b < a:
    #         print("The last number cannot be smaller than the first one.")
    #         sys.exit()
    # except:
    #     print("I am sorry, this is an invalid number. Please type in a "
    #             "valid one")
    #     sys.exit()

    _ = input("Ok, the game is about to start! Ready?")
    for number in range(a, b + 1):
        _ = input("The next number is... (Press any key to continue)")
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz!")
        elif number % 3 == 0:
            print("Fizz!")
        elif number % 5 == 0:
            print("Buzz!")
        # elif number % 3 == 0 and number % 5 == 0:
        #     print("Fizz Buzz!")
        else:
            print(number)


fizzbuzz()