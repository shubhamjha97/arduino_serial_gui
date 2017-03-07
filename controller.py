from serial import Serial

class component:
	def __init__(self, comp):
		print 'Initializing', comp,'.'
		self.ser=Serial('/dev/ttyACM0')
		print 'Serial connection established.'

	def ip(self, control):
		if control==True:
			control='1'
		else:
			control='0'
		self.ser.write(control)
		return 0
		#if error return 1