
from naoqi import ALProxy
from settings.Settings import Settings

class cmdExecuteBehavior(object):
	'''
	classdocs
	'''
	
	def __init__(self):
		self.cmd = "EXECUTE_BEHAVIOR"
	
	def exe(self, args=None, addr=None):
		
		# create proxy
		behaviorProxy = ALProxy('ALBehaviorManager', Settings.naoHostName, Settings.naoPort)
		
		# create sentence
		if len(args) > 0:	
			behaviorProxy.runBehavior(args[0])