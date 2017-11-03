#All validation functions that are not private should go here.


#This function should be private for the game engine.
def isGameOver(gameInfo):
    if(gameInfo["score"] <= -100):
    	return True

    return False

#This function should be part of the configuration manager class.
def confirmSave(answer):
	if answer == 'y' or answer == 'Y':
		return True
	return False

#Functions for data validation should come here.