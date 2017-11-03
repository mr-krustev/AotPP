import re
import validator
import time

def getConfig():
	controlsFile = open('controls.conf')
	curLine = controlsFile.readline();
	while(curLine):
		curLine = re.split(' |:|\n', curLine)
		contrConf[curLine[0]] = curLine[1]
		curLine = controlsFile.readline();

def saveConfig(newConf):
	"""Receives a new conf file to replace the old one."""
	for setting, value in newConf.items():
		contrConf[setting] = value


def updateConfig():
	newConf = {}
	for setting, value in contrConf.items():
		text = "Button for " + setting + ": "
		response = raw_input(text)
		response = re.split(' |;|:|\n|!', response)[0]
		if response == "":
			newConf[setting] = value
			continue
		newConf[setting] = response

	shouldSave = validator.confirmSave(raw_input("Save settings? [Y/N]: "))
	if shouldSave:
		saveConfig(newConf)
		raw_input("Press enter to continue")

def getControlsString():
	outputStr = ""
	for setting, value in contrConf.items():
		outputStr = outputStr + value + "=" + setting + " "
	return outputStr



contrConf = {}
getConfig()
print(getControlsString())