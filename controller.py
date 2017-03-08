from serial import Serial
import serial

class component:
	def __init__(self, comp):
		self.comp=comp
		'''try:
			print 'Initializing', comp,'.'
			self.ser=Serial('/dev/ttyACM0')
			print 'Serial connection established.'
		except serial.serialutil.SerialException:
			print "Didn't find Arduino on port"
			return None'''

	def connect(self):
		try:
			print 'Initializing', self.comp,'.'
			self.ser=Serial('/dev/ttyACM0')
			print 'Serial connection established.'
			return 0
		except serial.serialutil.SerialException:
			print "Didn't find Arduino on port"
			return 1

	def ip(self, control):
		if control==True:
			control='1'
		else:
			control='0'
		self.ser.write(control)
		return 0
		#if error return 1

if __name__=='__main__':
	a=component('led')