import random


def updateEnemy(gameInfo):
    gameInfo["enemyStrength"] = random.randrange(
        gameInfo["playerStrength"] // 2, gameInfo["playerStrength"] + 3)


def updateScore(gameInfo, hasWon, scoreAdjustment=1):
    if (hasWon):
        gameInfo["score"] = gameInfo["score"] + scoreAdjustment
    else:
        gameInfo["score"] = gameInfo["score"] - scoreAdjustment


def updateExp(gameInfo, hasAcquired):
    if(not hasAcquired):
        return
    gameInfo["playerExp"] = gameInfo["playerExp"] + gameInfo["enemyStrength"]


def updatePlayerLevelUp(gameInfo, hasEnoughExp):
    if(hasEnoughExp):
        gameInfo["playerStrength"] = gameInfo[
            "playerStrength"] + gameInfo["playerLevel"] * 2
        gameInfo["playerLevel"] = gameInfo["playerLevel"] + 1
        gameInfo["playerExp"] = gameInfo[
            "playerExp"] - gameInfo["expForNextLevel"]
        gameInfo["expForNextLevel"] = gameInfo["expForNextLevel"] * 2
    else:
        updateScore(gameInfo, hasEnoughExp, gameInfo["enemyStrength"])
