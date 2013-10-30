def CheckIfPalindrome(Word):
	reverseWord = Word[::-1]
	if (Word==reverseWord):
		print True
	else:
		print False





if __name__ == "__main__":
	Word = raw_input("Enter word: ")	
	CheckIfPalindrome(Word)
	
