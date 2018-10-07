from .PointLoad import PointLoads
from .Analyze import BeamAnalysis
from .AnalysisResults import Results
from .DrawLoadDia import LoadingDiagram
import matplotlib.pyplot as plt

class Beam:
    def __init__(self,spanLength):
        self.Span = spanLength
        self.Loads = []
        self.Results = Results
        
    def SetLoads(self,loadIntensity, distFromLeft):
        for load in range(0,len(loadIntensity)):
            self.Loads.append(PointLoads(loadIntensity[load], distFromLeft[load]))
            
    def GetResults(self):
         self.LeftReaction, self.RightReaction = BeamAnalysis.CalcReactions(self.Loads,self.Span)
    
    def Draw(self, normalisationValue):
        fig = plt.figure()
        ax = plt.axes()
        LoadingDia = LoadingDiagram(normalisationValue)
        LoadingDia.DrawBoundingBox(ax, self.Span)
        LoadingDia.DrawSpan(ax, self.Span)
        for load in self.Loads:
            LoadingDia.DrawLoadsAndReactions(ax, [load.Intensity], [load.DistFromLeftEnd], False)
        LoadingDia.DrawLoadsAndReactions(ax, [self.LeftReaction, self.RightReaction], [0,self.Span], True)
        plt.show()