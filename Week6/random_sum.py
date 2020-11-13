import random
rand_num_1 = random.randint(0, 12)
rand_num_2 = random.randint(0, 12)

result = rand_num_1 * rand_num_2
#print(rand_num_1)
#print(rand_num_2)
#print(result)

while True:
    answer = int(input("What is " + str(rand_num_1) + "*" + str(rand_num_2)))
    #print(type(answer))
    #print(type(result))
    if answer == result:
        print("Well done!")
        break
    else:
        print("Try again!")
