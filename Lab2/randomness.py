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
def CoinFlip3(Flip):
	z = 0	
	while (z<Flip):
		rand = randint(0,1)		
		if (rand==0):
			print "H"
		else:
			print "T"
		z+=1

if __name__ == "__main__":
	Flip = int(raw_input("how many flips?"))
	CoinFlip3(Flip)
		
