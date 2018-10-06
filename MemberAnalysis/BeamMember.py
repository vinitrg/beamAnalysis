from .PointLoad import PointLoads

class Beam:
    def __init__(self,spanLength):
        self.Span = spanLength
        self.Loads = []
        
    def SetLoads(self,loadIntensity, distFromLeft):
        for load in range(0,len(loadIntensity)):
            self.Loads.append(PointLoads(loadIntensity[load], distFromLeft[load]))