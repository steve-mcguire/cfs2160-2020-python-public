import random
secret_number = random.randint(0, 101)

print(secret_number)
counter = 1
while True:
    try:
        response = int(input("Please guess a number"))
        # print(type(response))
        # print(response)
        if response not in range(0, 101):
            print("Out of range")
        else:
            if response == secret_number:
                print("Well done")
                print("You took {} guesses".format(counter))
                break
            elif response > secret_number:
                print("Your guess is too high")

            else:
                print("Your guess is too low")

            counter += 1
    except ValueError:
        print("Please enter a number between zero and 100")








print(counter)

