from random import randint
def CoinFlip(n):
	randomNum = randint(0,10)
	if (n=="n"):
		if (randomNum%2==0):
			return "H"
		else:
			return "T"
def CoinFlip2(n,prob):
	randomNum = randint(0,100)
	if (n=="n"):
		if (randomNum<=prob):
			return "H"
		else:
			return "T"

if __name__ == "__main__":
	prob = int(raw_input("what is the probability of heads?"))
	n = raw_input("press n to flip")
	print CoinFlip2(n,prob)
		
