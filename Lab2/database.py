def database():
	dictionary = {}
	x = 0
	while (x<3):
		name = raw_input("Enter name: ")
		age = raw_input("Enter age: ")		
		dictionary[name] = age
		x+=1
	print dictionary
	




if __name__ == "__main__":
	database()
