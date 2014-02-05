class Integer(object):
	
	def __init__(self, num, PN):
		self.number = num
		self.PosNeg = PN
		
	def display(self):
		print self.PosNeg + str(self.number)

class NegativeInteger(Integer):
	
	def __init__(self, num):
		super(NegativeInteger, self).__init__(num, "-")
	def display(self):
		#print self.PosNeg + str(self.number) + " This is an object of the NegativeInteger class"
		Integer.display(self)
		print " This is an object of the NegativeInteger class"



if __name__=="__main__":
	
	obj = Integer(50, "+")
	obj1 = NegativeInteger(100)
	
	objects = [obj, obj1]

	for i in objects:
		i.display()
