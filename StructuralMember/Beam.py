from ..LoadInfo.PointLoad import *

class Beam:
    
    def __init__(self,spanLength):
        self.Span = spanLength
        
    def SetLoads(self,loadIntensity, distFromLeft):
        self.PointLoad = PointLoad(loadIntensity, distFromLeft)