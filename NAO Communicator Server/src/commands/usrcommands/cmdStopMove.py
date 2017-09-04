from naoqi import ALProxy
from settings.Settings import Settings

class cmdVelocityWalk(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.cmd = "STOP_MOVE"
    
    def exe(self, args=None, addr=None):
        
        
        # create proxy
        motion = ALProxy("ALMotion", Settings.naoHostName, Settings.naoPort)
        motion.stopMove()