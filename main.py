import msvcrt
import random
import time
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


def updateEnemy(gameInfo):
    gameInfo["enemyStrength"] = random.randrange(
        1, gameInfo["playerStrength"] + 3)


def updateScore(gameInfo, hasWon, scoreAdjustment=1):
    if (hasWon):
        gameInfo["score"] = gameInfo["score"] + scoreAdjustment
    else:
        gameInfo["score"] = gameInfo["score"] - scoreAdjustment


def updateExp(gameInfo, hasAcquired):
    if(hasAcquired == False):
        return
    gameInfo["playerExp"] = gameInfo["playerExp"] + gameInfo["enemyStrength"]


def updatePlayerLevelUp(gameInfo, hasEnoughExp):
    if(hasEnoughExp):
        gameInfo["playerStrength"] = gameInfo[
            "playerStrength"] + gameInfo["playerLevel"] * 2
        gameInfo["playerLevel"] = gameInfo["playerLevel"] + 1
        gameInfo["playerExp"] = 0
        gameInfo["expForNextLevel"] = gameInfo["expForNextLevel"] * 2
    else:
        updateScore(gameInfo, hasEnoughExp, gameInfo["enemyStrength"])


def playerDefend(gameInfo):
    hasWon = gameInfo["playerStrength"] == gameInfo["enemyStrength"]
    if (hasWon):
        print("Player won!")
    else:
        print("Player Lost!")

    updateExp(gameInfo, hasWon)
    updateScore(gameInfo, hasWon)
    updateEnemy(gameInfo)


def playerAttack(gameInfo):
    hasWon = gameInfo["playerStrength"] > gameInfo["enemyStrength"]
    if (hasWon):
        print("Player won!")
    else:
        print("Player Lost!")

    updateExp(gameInfo, hasWon)
    updateScore(gameInfo, hasWon)
    updateEnemy(gameInfo)


def playerHold(gameInfo):
    hasWon = gameInfo["playerStrength"] < gameInfo["enemyStrength"]
    if (hasWon):
        print("Player won!")
    else:
        print("Player Lost!")

    updateExp(gameInfo, hasWon)
    updateScore(gameInfo, hasWon)
    updateEnemy(gameInfo)


def playerLevelUp(gameInfo):
    hasEnoughExp = gameInfo["playerExp"] >= gameInfo["expForNextLevel"]
    if(hasEnoughExp):
        print("Leveled up!")
    else:
        print("Not enough experience, score penalty")
    updatePlayerLevelUp(gameInfo, hasEnoughExp)


def printInfoBar(gameInfo):
    info = "\nPlayer strength: ", gameInfo["playerStrength"], "\tExperience: ", gameInfo["playerExp"], "\tExpReq:", gameInfo["expForNextLevel"], "\tScore: ", gameInfo[
        "score"], "\nEnemy strength: ", gameInfo["enemyStrength"], "\nA=Attack,D=Defend,H=Hold,L=Level Up\n\n"
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


main()
