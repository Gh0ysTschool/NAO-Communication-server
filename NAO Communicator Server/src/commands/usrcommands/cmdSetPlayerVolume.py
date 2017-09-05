

from naoqi import ALProxy
from settings.Settings import Settings

class cmdSetPlayerVolume(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cmd = "SET_PLAYER_VOLUME"
        
    def exe(self, args=None, addr=None):
        
        # get proxies
        player = ALProxy("ALAudioPlayer", Settings.naoHostName, Settings.naoPort)
        
        # set system volume
        if len(args) > 0:
            player.setMasterVolume( float(args[0]) )