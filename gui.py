from Tkinter import *
import controller

class MyGUI:
	def __init__(self,root):
		self.root=root
		self.root.geometry('200x50')
		self.root.title('On/Off Button')
		on_off=Button(self.root, text='On/Off', command=self.toggle)
		on_off.pack()
		self.status=True

		self.status_var=StringVar()
		status=Label(self.root, textvariable=self.status_var)
		self.status_var.set("LED")
		status.pack()

	def toggle(self):
		self.status= not self.status
		led.ip(self.status)
		if self.status==False:
			self.status_var.set("LED is off.")
		else:
			self.status_var.set("LED is on.")

led=controller.component('led')
connection_status=led.connect()
if not connection_status:
	root=Tk()
	gui=MyGUI(root)
	root.mainloop()



