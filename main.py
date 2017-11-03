import msvcrt
import os

import updates
import validator
import controls
# This is where you start the APP.
# Currently it will hold the whole game as things are being
# moved to classes following OOP principles.


def takeActionByKey(key, gameInfo):
    if(key == controls.contrConf['quit']):
        return False
    elif(key == controls.contrConf['attack']):
        playerAttack(gameInfo)
    elif(key == controls.contrConf['defend']):
        playerDefend(gameInfo)
    elif(key == controls.contrConf['hold']):
        playerHold(gameInfo)
    elif(key == controls.contrConf['options']):
        controls.updateConfig()

    return True


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
        "score"], "\nEnemy strength: ", gameInfo["enemyStrength"], "\n" + controls.getControlsString() + "\n"
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
    enemyStrength = 0

    gameInfo = {"score": score,
                "playerStrength": playerStrength,
                "enemyStrength": enemyStrength,
                "playerExp": playerExp,
                "expForNextLevel": expForNextLevel,
                "playerLevel": playerLevel}

    updates.updateEnemy(gameInfo)
    os.system('cls')
    while isGameOn:
        printInfoBar(gameInfo)
        key = msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        hasPlayerLost = validator.isGameOver(gameInfo)
        isGameOn = takeActionByKey(key, gameInfo) and not hasPlayerLost

        if hasPlayerLost:
            print("Game over! You went below -100 score!")

main()
