import msvcrt

#This is where you start the APP.
#Currently it will hold the whole game as things are being 
#moved to classes following OOP principles.

def translateKey(key):
	if(key == "q"):
		return False
	elif(key == "a"):
		print "Attack"
	elif(key == "d"):
		print "Defend"
	elif(key == "h"):
		print "Hold"

	return True

def main():
	isGameOn = True
	while isGameOn:
		if msvcrt.kbhit():
			key = msvcrt.getch()
			isGameOn = translateKey(key)
			

main()