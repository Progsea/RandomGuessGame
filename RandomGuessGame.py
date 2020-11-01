# importing random
import random

# generating the random number
r = random.randint(1,10)

# user's guess/input
print("Input a number 1-10: ")
rInp = int(input())

# check if the user's guess is equal to the generated number.
# it will let the user know that they won.
# else, then it will let the user know that they lost.
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
