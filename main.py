import msvcrt
import random

# This is where you start the APP.
# Currently it will hold the whole game as things are being
# moved to classes following OOP principles.


def takeActionByKey(key, gameInfo):
    if(key == "q"):
        return False
    elif(key == "a"):
        playerAttack(gameInfo)
    elif(key == "d"):
        print "Defend"
    elif(key == "h"):
        print "Hold"

    return True


def playerAttack(gameInfo):
    if (gameInfo["playerStrength"] > gameInfo["enemyStrength"]):
        gameInfo["score"] = gameInfo["score"] + 1
        print("Player won!", gameInfo["score"])
    elif (gameInfo["playerStrength"] < gameInfo["enemyStrength"]):
        gameInfo["score"] = gameInfo["score"] - 1
        print("Player Lost!", gameInfo["score"])
    else:
        print("Draw!")

    gameInfo["enemyStrength"] = random.randrange(1, gameInfo["playerStrength"] + 3)
    return


def main():
    isGameOn = True
    score = 0
    playerStrength = 5
    enemyStrength = random.randrange(1, playerStrength)
    gameInfo = {"score": score, "playerStrength": playerStrength,
                "enemyStrength": enemyStrength}
    while isGameOn:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            isGameOn = takeActionByKey(key, gameInfo)


main()
