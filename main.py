import msvcrt
import random
import updates as updates
import os

# This is where you start the APP.
# Currently it will hold the whole game as things are being
# moved to classes following OOP principles.


def takeActionByKey(key, gameInfo):
    if(key == "q"):
        return False
    elif(key == "a"):
        playerAttack(gameInfo)
    elif(key == "d"):
        playerDefend(gameInfo)
    elif(key == "h"):
        playerHold(gameInfo)
    elif(key == "l"):
        playerLevelUp(gameInfo)

    return True


def isGameOver(gameInfo):
    if(gameInfo["score"] <= -100):
        return True

    return False


def playerDefend(gameInfo):
    hasWon = gameInfo["playerStrength"] == gameInfo["enemyStrength"]
    if (hasWon):
        print("Player won!")
    else:
        print("Player Lost!")

    updates.updateExp(gameInfo, hasWon)
    playerLevelUp(gameInfo)
    updates.updateScore(gameInfo, hasWon)
    updates.updateEnemy(gameInfo)


def playerAttack(gameInfo):
    hasWon = gameInfo["playerStrength"] > gameInfo["enemyStrength"]
    if (hasWon):
        print("Player won!")
    else:
        print("Player Lost!")

    updates.updateExp(gameInfo, hasWon)
    playerLevelUp(gameInfo)
    updates.updateScore(gameInfo, hasWon)
    updates.updateEnemy(gameInfo)


def playerHold(gameInfo):
    hasWon = gameInfo["playerStrength"] < gameInfo["enemyStrength"]
    if (hasWon):
        print("Player won!")
    else:
        print("Player Lost!")

    updates.updateExp(gameInfo, hasWon)
    playerLevelUp(gameInfo)
    updates.updateScore(gameInfo, hasWon)
    updates.updateEnemy(gameInfo)


def playerLevelUp(gameInfo):
    hasEnoughExp = gameInfo["playerExp"] >= gameInfo["expForNextLevel"]
    if(hasEnoughExp):
        print("Leveled up!")
    updates.updatePlayerLevelUp(gameInfo, hasEnoughExp)


def printInfoBar(gameInfo):
    info = "\nPlayer strength: ", gameInfo["playerStrength"], "\tExperience: ", gameInfo["playerExp"], "\tExpReq:", gameInfo["expForNextLevel"], "\tScore: ", gameInfo[
        "score"], "\nEnemy strength: ", gameInfo["enemyStrength"], "\nA=Attack,D=Defend,H=Hold\n"
    infoBar = map(str, info)
    print(''.join(infoBar))


def main():
    isGameOn = True
    # gameInfo
    score = 0
    # playerInfo
    playerStrength = 5
    playerLevel = 1
    playerExp = 0
    expForNextLevel = 15
    # enemyInfo
    enemyStrength = random.randrange(1, playerStrength)

    gameInfo = {"score": score,
                "playerStrength": playerStrength,
                "enemyStrength": enemyStrength,
                "playerExp": playerExp,
                "expForNextLevel": expForNextLevel,
                "playerLevel": playerLevel}
    os.system('cls')
    while isGameOn:
        printInfoBar(gameInfo)
        key = msvcrt.getch()
        os.system('cls')
        isGameOn = takeActionByKey(key, gameInfo)
        if isGameOn:
            isGameOn = not isGameOver(gameInfo)
            print("Game over! You went below -100 score!")

main()
