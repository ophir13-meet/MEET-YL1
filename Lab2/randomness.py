from random import randint
def CoinFlip(n):
	randomNum = randint(1,10)
	if (n=="n"):
		if (randomNum%2==0):
			return "H"
		else:
			return "T"

if __name__ == "__main__":
	n = raw_input("press n to flip")
	print CoinFlip(n)
		
