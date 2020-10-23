#loop n times until a conditon is met

password = "password"

while True:
    user_input = input("Please enter your password").lower()
    #print(user_input)

    result = user_input == password
    print(result)
    if result:
        print("inputs match")
        break
    else:
        print("Inputs do not match, please try again")

print("Loop ended as condition found")
