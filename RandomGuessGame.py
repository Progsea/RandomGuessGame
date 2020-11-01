import random
# setting random num variable
r = random.randint(1,10)

# asking the user to input their guess between 1-10
print("Input a number 1-10: ")
rInp = int(input())

# checking if the random number is the same as the input the user has given
if r == rInp:
    # if user wins the command prompt will let the user know that they have won
    print("You win!")
    input()
    exit()
else:
    # if user loses the command prompt will let the user know that they have lost
    print("Aww.. you lost!")
    print("The random number was " + str(r))
    print("Press enter to end.")
    input()
    exit()
