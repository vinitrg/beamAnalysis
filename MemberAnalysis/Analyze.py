from .PointLoad import PointLoads
from .AnalysisResults import Results

class BeamAnalysis:
    def CalcReactions(Loads, length):
        rightReactions = 0
        leftReactions = 0        
        for load in Loads:
            rightReaction = load.Intensity*load.DistFromLeftEnd / length
            leftReaction = load.Intensity - rightReaction
            rightReactions += rightReaction
            leftReactions += leftReaction
        return(leftReactions,rightReactions)