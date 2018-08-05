from pykd import *

class Handler(eventHandler):
	def __init__(self):
		initialize()
		eventHandler.__init__(self)
		startProcess('bob.exe')
		
