import random
# hello world
r = random.randint(1,10)

print("Input a number 1-10: ")
rInp = int(input())

if r == rInp:
    print("You win!")
    input()
    exit()
else:
    print("Aww.. you lost!")
    print("The random number was " + str(r))
    print("Press enter to end.")
    input()
    exit()
