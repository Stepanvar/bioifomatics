import random
flag = 1
def letters_in_log(name):
    name = list(name.lower())
    x = 2
    login_letters = random.choice(name)
    while x > 0:
        login_letters += random.choice(name)
        x -= 1
    login_letters = login_letters[0].upper() + login_letters[1:]
    return(login_letters)
name = input("enter your name and i will generate your login\n")
print("good name " + name + " but now we will make it better")
print("wait...")
login = letters_in_log(name) + str(random.randint(1, 77))
print("Your login is", login, sep= " ")
print("Hello, " + login + " let's play:")
res_dice = random.randint(1, 10)
while flag != 0:
    while res_dice in range(1,7):
        res_dice = random.randint(1, 10)
        if res_dice == 7:
            res_dice -= 3
            print("your dice get %2d" %(res_dice), " continue")
        elif res_dice == 8:
            res_dice -= 4
            print("your dice get %2d" %(res_dice) + " continue")
        elif res_dice == 9:
            print("your cheat dice get %d game over" %res_dice)
        elif res_dice > 9:
            res_dice -= 5
            print("your dice get %2d" %(res_dice) + " continue")
        else:
            print("your dice got " + str(res_dice) + " continue")
    else:
        answer = int(input("wanna try 1 more time? 1 - yes, 2 - no\n"))
        if answer == 1:
            flag += 1
            res_dice = 1
        else:
            print("you play %d" %flag, "time(s)\nGood job!\nBye")
            flag = 0